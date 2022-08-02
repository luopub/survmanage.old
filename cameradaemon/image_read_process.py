import cv2 as cv
import numpy as np
from PIL import Image
import time
import os
import ctypes
from yolov5 import YOLOv5
from multiprocessing import Process, Queue, Manager, Array

from .image_client import ImageClient
from .image_server_code import *
from .utils import save_raw_frame


class ImageStreamProcess(Process):
    def __init__(self, camera):
        super(ImageStreamProcess, self).__init__(target=self.process_loop)
        self.queue_size = 25
        self.raw_img_queue = Queue(self.queue_size)
        self.camera = Manager().Value(ctypes.c_char_p, camera)
        self.online = Manager().Value(ctypes.c_int, 0)

    def change_camera(self, camera):
        self.camera.value = camera

    def process_loop(self):
        print('Process to write: %s' % os.getpid())
        while True:
            camera = self.camera.value
            t1 = time.time()
            print('Start VideoCapture', camera)
            cap = cv.VideoCapture(camera)
            print('Time used for start camera: ', time.time() - t1)
            if cap.isOpened() and cap.read()[0]:
                self.online.value = 1

                # If continuous fail, then the camera may be off line
                fail_count = 0
                frame_count = 0
                while True:
                    rv, img = cap.read()
                    if not rv:
                        fail_count += 1
                        if fail_count >= 10:
                            break
                        time.sleep(0.1)
                        continue

                    fail_count = 0

                    try:
                        self.raw_img_queue.put_nowait(img)
                    except:
                        pass

                    frame_count += 1

                    if frame_count % 25 == 0:
                        # 隔段时间检测是否改变了地址
                        if camera != self.camera.value:
                            break

            print('camera is offline!')
            self.online.value = 0
            # Wait for some time to try again
            cap.release()
            time.sleep(10)


class ImageConsumeProcess(Process):
    def __init__(self, cno, raw_img_queue, model_path=None, model_device=None, predict_threshold=0.5):
        super(ImageConsumeProcess, self).__init__(target=self.process_loop)
        self.cno = cno
        self.raw_img_queue = raw_img_queue
        # 分配一个足够大的buffer暂存最后一张图片
        self.latest_img = Array(ctypes.c_int, np.zeros((1280*1280*3, ), dtype=np.uint8), lock=True)
        self.latest_img_interval = 1000  # In milliseconds
        self.predict_interval = 1000  # In milliseconds
        self.img_size = Array(ctypes.c_int, np.zeros((3, )).astype(int), lock=True)
        self.model = None
        self.model_path = model_path
        self.model_device = model_device
        self.predict_threshold = predict_threshold

    def set_params(self, latest_img_interval=None, predict_interval=None, predict_threshold=None):
        """
        设置参数, 这些原子数据类型不用同步类型
        """
        if latest_img_interval is not None:
            self.latest_img_interval = latest_img_interval

        if predict_interval is not None:
            self.predict_interval = predict_interval

        if predict_threshold is not None:
            self.predict_threshold = predict_threshold

    def init_model(self):
        if self.model_path:
            self.model = YOLOv5(self.model_path, device=self.model_device)

    def predict_single_frame(self, raw_frame):
        # 格式转变，BGRtoRGB
        frame = cv.cvtColor(raw_frame, cv.COLOR_BGR2RGB)
        results = self.model.predict(frame)

        if len(results.pred[0]):
            # 过滤掉小于threshold的结果
            results.pred[0] = results.pred[0][results.pred[0][:, -2] >= self.predict_threshold]

            pred = results.pred[0].numpy()
            if pred.shape[0]:
                filename = save_raw_frame(results.render()[0], cno=self.cno, cvt_color=False)

                # 结果转换成便于处理的结果
                predicts = [
                    {
                        'confidence': float(p[-2]),
                        'name': results.names[int(p[-1])]
                    }
                    for p in pred
                ]

                res = ImageClient(IMG_CMD_OBJECT_DETECTED, cno=self.cno, filename=filename, predicts=predicts).do_request(wait_result=False)
                if res and res['code'] == IMG_CODE_SUCCESS:
                    pass

    # 在缓冲栈中读取数据:
    def process_loop(self):
        print('Process to read: %s' % os.getpid())
        self.init_model()
        # 开始时间
        t1 = time.time()  # 最新图片保存定时
        t2 = time.time()  # 预测定时

        frame_count = 0
        while True:
            try:
                value = self.raw_img_queue.get(timeout=1)
            except:  # Queue.Empty
                continue

            frame_count += 1

            # 格式转变，BGRtoRGB
            # frame = cv.cvtColor(value, cv.COLOR_BGR2RGB)
            # 转变成Image
            # frame = Image.fromarray(np.uint8(frame))
            frame = value

            if (time.time() - t2) * 1000 > self.predict_interval:
                t2 = time.time()
                self.predict_single_frame(frame)

            if (time.time() - t1) * 1000 > self.latest_img_interval:
                t1 = time.time()

                # print("raw_img_queue length", self.raw_img_queue.qsize(), frame_count)
                frame_count = 0

                # 每隔一小段时间保存一次最新图像
                self.img_size[:] = frame.shape

                # print("raw_img_queue length 1", self.img_size[:], frame.dtype)

                self.latest_img[:frame.shape[0]*frame.shape[1]*frame.shape[2]] = frame.astype(np.uint8).reshape((-1, ))

    def get_latest_image(self):
        try:
            height, width, depth = self.img_size[:]
            # print("get_latest_image", height, width, depth)
            if height * width * depth:
                return np.array(self.latest_img[:height*width*depth]).astype(np.uint8).reshape(height, width, depth)
        except:
            pass
