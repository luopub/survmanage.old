import cv2 as cv
import numpy as np
from PIL import Image
import time
import os
import ctypes

from multiprocessing import Process, Queue, Manager


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
    def __init__(self, raw_img_queue):
        super(ImageConsumeProcess, self).__init__(target=self.process_loop)
        self.raw_img_queue = raw_img_queue
        self.latest_img = Queue(1)

    # 在缓冲栈中读取数据:
    def process_loop(self):
        print('Process to read: %s' % os.getpid())
        # 开始时间
        t1 = time.time()

        frame_count = 0
        while True:
            try:
                value = self.raw_img_queue.get(timeout=1)
            except:  # Queue.Empty
                continue

            frame_count += 1

            # 格式转变，BGRtoRGB
            frame = cv.cvtColor(value, cv.COLOR_BGR2RGB)
            # 转变成Image
            # frame = Image.fromarray(np.uint8(frame))

            if int(time.time() - t1) >= 1:
                t1 = time.time()

                print("raw_img_queue length", self.raw_img_queue.qsize(), frame_count)
                frame_count = 0

                # 每隔一小段时间保存一次最新图像
                try:
                    self.latest_img.get_nowait()
                except:
                    pass
                self.latest_img.put(frame)

    def get_latest_image(self):
        try:
            return self.latest_img.get_nowait()
        except:
            pass


class ImageProcessPair:
    def __init__(self, camera):
        self.camera = camera
        self.raw_img_queue = None
        self.pw = None
        self.pr = None

    def start(self):
        # pw = Process(target=write, args=(q, rtsp_url, queue_size))
        self.pw = ImageStreamProcess(self.camera)
        self.pr = ImageConsumeProcess(self.pw.raw_img_queue)
        # 启动子进程pw，写入:
        self.pw.start()
        # 启动子进程pr，读取:
        self.pr.start()
