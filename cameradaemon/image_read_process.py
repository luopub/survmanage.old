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
                t1 = time.time()
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

                    if time.time() - t1 >= 1:
                        t1 = time.time()
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

    @staticmethod
    def time_in_alert_times(alert_times, local_time=None):
        """
        检测local_time是否在alert_times范围内
        """
        if not alert_times:
            return False

        if not local_time:
            local_time = time.localtime()

        this_day = alert_times[local_time.tm_wday]
        if not this_day['enabled'] or not this_day['segs']:
            return False

        minutes = local_time.tm_hour * 60 + local_time.tm_min
        for s in this_day['segs']:
            if s[0] <= minutes < s[1]:
                return True
            if minutes < s[0]:
                return False

        return False

    @staticmethod
    def rect_intersect(r1, r2):
        """
        判断两个矩形是否相交。
        如果相交，两个矩形的最小外接矩形的宽度和高度都小于两个矩形独自宽度和高度之和
        """
        return (max(r1[2], r2[2]) - min(r1[0], r2[0]) < r1[2] - r1[0] + r2[2] - r2[0]
            and max(r1[3], r2[3]) - min(r1[1], r2[1]) < r1[3] - r1[1] + r2[3] - r2[1])

    @classmethod
    def pred_in_roi_region(cls, roi_region, pred):
        """
        如果没有roi区域，认为是全域检测
        """
        if not roi_region:
            return True
        for r in roi_region:
            if cls.rect_intersect([r['x1'], r['y1'], r['x2'], r['y2']], pred):
                return True

        return False

    def addRoiRegion(self, results, regions, index):
        colors = [
            # [128, 0, 0],
            # [0, 128, 0],
            [0, 0, 128]
        ]
        for i in index:
            if not regions[i]:
                continue
            for r in regions[i]:
                blk = np.zeros(results.imgs[0].shape, np.uint8)
                cv.rectangle(blk, [r['x1'], r['y1']], [r['x2'], r['y2']], colors[i % len(colors)], -1)
                results.imgs[0] = cv.addWeighted(results.imgs[0], 1.0, blk, 0.4, 1)

    def predict_single_frame(self, raw_frame, cno=0):
        try:
            # 检查是否有新参数
            cas = self.cas_queue.get_nowait()
            # 添加一些键值，便于后续处理
            for ca in cas:
                # 上一次检测时间
                ca['last_predict_time'] = time.time() - ca['analyze_interval'] / 1000  # 减去间隔以便能够立刻开始检测
                # 上一次报警时间
                ca['last_alert_time'] = time.time() - ca['alert_interval']  # 减去间隔以便能够立刻开始报警
            self.cas = cas
        except:
            pass

        # 只选取指定通道的参数
        cas = [ca for ca in self.cas if ca['channel__cno'] == cno]

        # 如果当前通道没有检测参数，就不用检测
        if not cas:
            return

        # 过滤符合检测时间的算法参数
        avail_cas = []
        for ca in cas:
            # 当前时间在布控时间范围才需要检测
            if not self.time_in_alert_times(ca['alert_times']):
                continue
            # 报警间隔足够才往下执行
            if time.time() - ca['last_alert_time'] < ca['alert_interval']:
                continue
            # 检测间隔足够就可以检测一次
            if (time.time() - ca['last_predict_time']) * 1000 >= ca['analyze_interval']:
                ca['last_predict_time'] = time.time()
                avail_cas.append(ca)

        if not avail_cas:
            return

        # 格式转变，BGRtoRGB
        frame = cv.cvtColor(raw_frame, cv.COLOR_BGR2RGB)
        # Results结构参考yolov5源代码Detections.(\yolov5\models\common.py)
        results = self.model.predict(frame)

        # 如果没有检测到任何分类，直接返回
        if len(results.pred[0]) == 0:
            return

        # 取得分类索引对应的阈值和roi区域
        thresholds = {results.names.index(ca['model_name']): ca['alert_threshold'] for ca in avail_cas}
        regions = {results.names.index(ca['model_name']): ca['roi_region'] for ca in avail_cas}

        # 过滤掉小于threshold或者不在roi_region的结果
        index = []
        pred = results.pred[0].numpy()
        for i in range(pred.shape[0]):
            # 保留能识别并且阈值足够大的结果类别
            class_index = pred[i, -1]
            confidence = pred[i, -2]
            if class_index in thresholds and confidence >= thresholds[class_index] and self.pred_in_roi_region(regions[class_index], pred[i]):
                index.append(i)

        results.pred[0] = results.pred[0][index, :]

        pred = results.pred[0]
        if not pred.shape[0]:
            # 如果没有合适结果，直接返回
            return

        # 首先保存未标注的图片
        img_unmark = save_raw_frame(results.imgs[0], cno=cno, cvt_color=False)

        self.addRoiRegion(results, regions, index)
        # 首先将识别结果图片生成
        img = save_raw_frame(results.render()[0], cno=cno, cvt_color=False)

        # 同一个类别只保留一个记录
        classes = set()
        remain_rows = []
        for i in range(pred.shape[0]):
            if pred[i, -1] not in classes:
                classes.add(pred[i, -1])
                remain_rows.append(i)

        pred = pred[remain_rows, :]

        predicts = [{
            'confidence': float(p[-2]),
            'name': results.names[int(p[-1])]
        } for p in pred]

        # 设置最后报警时间
        for p in pred:
            for ca in avail_cas:
                if results.names[int(p[-1])] == ca['model_name']:
                    ca['last_alert_time'] = time.time()
                    break

        print(f'{cno}-predicts', predicts)

        # 保存报警信息
        ImageClient(IMG_CMD_OBJECT_DETECTED, cno=cno, img_unmark=img_unmark, img=img, predicts=predicts).do_request(wait_result=False)


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
