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


DEFAULT_DETECT_TICK = 500  # 默认检测500毫秒为单位
DEFAULT_LATEST_IMAGE_INTERVAL = 1000  # 默认保存最新图片间隔
MAX_IMAGE_WIDTH = 1920
MAX_IMAGE_HEIGHT = 1080
DEFAULT_IMAGE_DEPTH = 3


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


class DetectionModel:
    def __init__(self, model_path, model_device):
        self.model = None
        self.model_path = model_path
        self.model_device = model_device
        self.predict_threshold = 0.5
        self.max_continous_predict = 30
        self.predicts_count = dict()  # 保存前面几次的预测结果，如果未超过max_continous_predict， 就不多次保存
        self.cas_queue = Queue(1)  # 接收传入参数
        self.cas = []  # ChannelAlgorithm parameters from, list of

    def init_model(self):
        if self.model_path:
            self.model = YOLOv5(self.model_path, device=self.model_device)

    def set_params(self, cas):
        """
        配置通道算法，数据来源于数据表：ChannelAlgorithm
        """
        self.cas_queue.put(cas)

    def predict_single_frame(self, raw_frame, cno=0):
        try:
            # 检查是否有新参数
            cas = self.cas_queue.get_nowait()
            self.cas = cas
        except:
            pass

        # 只选取指定通道的参数
        cas = [ca for ca in self.cas if ca['channel__cno'] == cno]

        # 如果当前通道没有检测参数，就不用检测
        if not cas:
            return

        # 过滤符合检测时间的参数，并且为新检测参数添加计时器
        avail_cas = []
        for ca in cas:
            if 'last_predict_time' not in ca:
                ca['last_predict_time'] = time.time()
            elif (time.time() - ca['last_predict_time']) * 1000 >= ca['analyze_interval']:
                ca['last_predict_time'] = time.time()
                avail_cas.append(ca)

        if not avail_cas:
            return
        
        # 格式转变，BGRtoRGB
        frame = cv.cvtColor(raw_frame, cv.COLOR_BGR2RGB)
        # Results结构参考yolov5源代码Detections.(\yolov5\models\common.py)
        results = self.model.predict(frame)

        # 获取当前通道的预测计数
        if cno not in self.predicts_count:
            self.predicts_count[cno] = dict()

        predicts_count = self.predicts_count[cno]

        if len(results.pred[0]) == 0:
            # 如果这次没有有效报警，那么清掉所有计数
            predicts_count.clear()
            return

        # 根据检测参数过滤检测结果

        # 过滤掉小于threshold的结果
        results.pred[0] = results.pred[0][results.pred[0][:, -2] >= self.predict_threshold]

        pred = results.pred[0].numpy()
        if pred.shape[0]:
            filename = save_raw_frame(results.render()[0], cno=cno, cvt_color=False)

            # 同一个类别只保留一个记录
            classes = set()
            remain_rows = []
            for i in range(pred.shape[0]):
                if pred[i][-1] not in classes:
                    classes.add(pred[i][-1])
                    remain_rows.append(i)

            pred = pred[remain_rows, :]

            # 结果转换成便于处理的结果
            predicts = [
                {
                    'confidence': float(p[-2]),
                    'name': results.names[int(p[-1])]
                }
                for p in pred
            ]

            new_names = set([p['name'] for p in predicts])

            print(f'{cno}-Detected 1', new_names)

            # 检测是否有保存的之前结果这次是否还在
            pre_names = list(predicts_count.keys())
            for name in pre_names:
                if name in new_names:
                    # 增加检测到的次数
                    predicts_count[name] += 1

                    if predicts_count[name] >= self.max_continous_predict:
                        # 但是连续出现持续时间够长，还是要间隔一段时间报警一次
                        predicts_count[name] = 1
                    else:
                        # 如果最近短期内有报警过，就不再继续报警。
                        new_names.discard(name)
                else:
                    # 如果旧的报警没有再次出现，就不再计数
                    del predicts_count[name]

            # 新的报警增加计数
            for name in new_names:
                if name not in predicts_count:
                    predicts_count[name] = 1

            print(f'{cno}-Detected 2', new_names)

            if new_names:
                # 清掉不需要的报警
                predicts = [p for p in predicts if p['name'] in new_names]
                res = ImageClient(IMG_CMD_OBJECT_DETECTED, cno=cno, filename=filename, predicts=predicts).do_request(wait_result=False)
                if res and res['code'] == IMG_CODE_SUCCESS:
                    pass


class ImageConsumeProcess(Process):
    def __init__(self, cno, raw_img_queue, model_path=None, model_device=None):
        super(ImageConsumeProcess, self).__init__(target=self.process_loop)
        self.cno = cno
        self.raw_img_queue = raw_img_queue
        # 分配一个足够大的buffer暂存最后一张图片
        self.latest_img = Array(ctypes.c_int, np.zeros((MAX_IMAGE_WIDTH*MAX_IMAGE_HEIGHT*DEFAULT_IMAGE_DEPTH, ), dtype=np.uint8), lock=True)
        self.img_size = Array(ctypes.c_int, np.zeros((3, )).astype(int), lock=True)
        self.model = DetectionModel(model_path, model_device)

    def set_params(self, cas):
        """
        设置参数, 这些原子数据类型不用同步类型
        """
        self.model.set_params(cas)

    # 在缓冲栈中读取数据:
    def process_loop(self):
        print('Process to read: %s' % os.getpid())
        self.model.init_model()
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

            if (time.time() - t2) * 1000 > DEFAULT_DETECT_TICK:
                t2 = time.time()
                self.model.predict_single_frame(frame, cno=self.cno)

            if (time.time() - t1) * 1000 > DEFAULT_LATEST_IMAGE_INTERVAL:
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
