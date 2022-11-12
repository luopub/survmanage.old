import cv2 as cv
import numpy as np
import time
import os
import ctypes
from yolov5 import YOLOv5
import multiprocessing
from multiprocessing import Process, Manager, Array
from threading import Thread
import queue

from utils.datetime_utils import datetime_utc_to_local

from .image_client import ImageClient
from .image_server_code import *
from .utils import save_raw_frame

from utils.logutils import get_logger
logger = get_logger(__file__)


DEFAULT_DETECT_TICK = 500  # 默认检测500毫秒为单位
DEFAULT_LATEST_IMAGE_INTERVAL = 1000  # 默认保存最新图片间隔
MAX_IMAGE_WIDTH = 2560
MAX_IMAGE_HEIGHT = 1440
DEFAULT_IMAGE_DEPTH = 3

ADDR_CHECK_INTERVAL = 1.0
SAMPLE_INTERVAL = 1.0  # Time interval to sample images from stream


class ImageProcess(Process):
    def __init__(self, cno, model_path=None, model_device=None):
        super(ImageProcess, self).__init__(target=self.process_loop)
        self.cno = cno
        self.queue_size = 25
        self.raw_img_queue = None  # Queue(self.queue_size)

        self.model_path = model_path
        self.model_device = model_device

        self.consume_thread = None  # ImageConsumeThread(self, model_path=model_path, model_device=model_device)
        self.read_thread = None  # ImageReadThread(self, camera)

        self.camera = Manager().Value(ctypes.c_char_p, '')
        self.online = Manager().Value(ctypes.c_int, 0)

        self.latest_img = Array(ctypes.c_int, np.zeros((MAX_IMAGE_WIDTH*MAX_IMAGE_HEIGHT*DEFAULT_IMAGE_DEPTH, ), dtype=np.uint8), lock=True)
        self.img_size = Array(ctypes.c_int, np.zeros((3, )).astype(int), lock=True)

        self.cas_queue = multiprocessing.Queue(1)  # 接收传入参数

        logger.info(f'ImageProcess inited: {cno}')

    def process_loop(self):
        self.raw_img_queue = queue.Queue(self.queue_size)
        self.read_thread = ImageReadThread(self)
        self.consume_thread = ImageConsumeThread(self, model_path=self.model_path, model_device=self.model_device)

        self.consume_thread.start()
        self.read_thread.start()

        self.read_thread.join()
        self.consume_thread.join()

    def set_params(self, cas):
        """
        配置通道算法，数据来源于数据表：ChannelAlgorithm
        """
        self.cas_queue.put(cas)

    def get_camera(self):
        return self.camera.value

    def set_camera(self, camera):
        self.camera.value = camera

    def get_online(self):
        return self.online.value

    def set_oneline(self, online):
        self.online.value = online

    def save_latest_image(self, frame):
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


class ImageReadThread(Thread):
    def __init__(self, process):
        super(ImageReadThread, self).__init__(target=self.process_loop)
        self.process = process
        self.cno = process.cno
        self.raw_img_queue = process.raw_img_queue

    def process_loop(self):
        cno = self.cno
        logger.info(f'{cno}-Process to write: {os.getpid()}')
        while True:
            camera = self.process.get_camera()
            if not camera:
                time.sleep(5)
                continue

            t1 = time.time()
            logger.info(f'{cno}-Start VideoCapture: {camera}')
            cap = cv.VideoCapture(camera)
            logger.info(f'{cno}-Time used for start camera: {time.time() - t1}')

            if cap and cap.isOpened() and cap.read()[0]:
                self.process.set_oneline(1)

                next_frame = cap.get(cv.CAP_PROP_POS_FRAMES)
                fps = cap.get(cv.CAP_PROP_FPS)

                logger.info(f'{cno}-fps={fps}, size={int(cap.get(cv.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))}, next frame={next_frame}')

                # If continuous fail, then the camera may be off line
                fail_count = 0
                frame_count = 0
                loose_count = 0
                save_count = 0
                timer_addr_check = time.time()
                timer_sample_interval = time.time()
                frame_to_skip = 0
                while True:
                    cap.grab()
                    frame_to_skip += 1
                    if frame_to_skip < 5:
                        continue
                    frame_to_skip = 0

                    rv, img = cap.retrieve()
                    if not rv:
                        fail_count += 1
                        if fail_count >= 10:
                            break
                        time.sleep(0.1)
                        continue

                    next_frame = cap.get(cv.CAP_PROP_POS_FRAMES)

                    frame_count += 1

                    # If all frames are saved, the reader may loose as much as 96% frames, so sample frame 1 per SAMPLE_INTERVAL
                    if time.time() - timer_sample_interval < SAMPLE_INTERVAL:
                        continue

                    timer_sample_interval = time.time()

                    fail_count = 0

                    save_count += 1
                    try:
                        self.raw_img_queue.put_nowait(img.copy())
                    except Exception as e:
                        loose_count += 1

                    if save_count % 10 == 0:
                        logger.info(f'{cno}-stream frame_count={frame_count}, save_count={save_count}, loose_count={loose_count}, {img.shape}, {self.raw_img_queue.qsize()}, {self.raw_img_queue.empty()}, {self.raw_img_queue.full()}, {next_frame}')

                    if time.time() - timer_addr_check >= ADDR_CHECK_INTERVAL:
                        timer_addr_check = time.time()
                        # 隔段时间检测是否改变了地址
                        if camera != self.process.get_camera():
                            break

            logger.info(f'{cno}-camera is offline, camera url set to {self.process.get_camera()}.')
            self.process.set_oneline(0)
            # Wait for some time to try again
            if cap:
                cap.release()
            time.sleep(10)


class DetectionModel:
    def __init__(self, model_path, model_device, cas_queue):
        self.model = None
        self.model_path = model_path
        self.model_device = model_device
        self.cas_queue = cas_queue
        self.cas = []  # ChannelAlgorithm parameters from, list of

    def init_model(self):
        if self.model_path:
            # 非常奇怪：如果没有这两句显示，模型初始化会失败！！！
            import torch
            logger.info(f'torch.cuda.is_available(): {torch.cuda.is_available()}')
            logger.info(f'torch.cuda.device_count(): {torch.cuda.device_count()}')
            self.model = YOLOv5(self.model_path, device=self.model_device)

    @staticmethod
    def time_in_alert_times(alert_times, local_time=None):
        """
        检测local_time是否在alert_times范围内
        """
        if not alert_times:
            return False

        if not local_time:
            # 获取当前北京时间
            local_time = datetime_utc_to_local().timetuple()

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

    @classmethod
    def pred_in_roi_region(cls, roi_region, pred):
        """
        如果没有roi区域，认为是全域检测
        """
        if not roi_region:
            return True

        # 检查4个点是否在多边形内
        lt = np.array([pred[0], pred[1]])
        rt = np.array([pred[2], pred[1]])
        rb = np.array([pred[2], pred[3]])
        lb = np.array([pred[0], pred[3]])
        for r in roi_region:
            for pt in [lt, rt, rb, lb]:
                if cv.pointPolygonTest(np.array(r), pt, True) > 0:
                    return True

        return False

    def addRoiRegion(self, results, regions, index):
        """
        Add ROI regions on picture
        results: results from model prediction
        regions: dict of regions, indexed by class index
        index: class index
        """
        color = [0, 0, 128]
        for i in index:
            if not regions[i]:
                continue
            blk = np.zeros(results.ims[0].shape, np.uint8)
            # Multiple polygons should be drawn one by one. Otherwise, some polygons can't be drawn together.
            for pts in regions[i]:
                cv.fillPoly(blk, np.array(pts)[np.newaxis, :], color=color, lineType=cv.LINE_4)

            results.ims[0] = cv.addWeighted(results.ims[0], 1.0, blk, 0.4, 1)

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

        # debug0820
        # import json
        # print('predict_single_frame ', time.time(), json.dumps(self.cas))

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

        # 如果在cuda上，先转成cpu再进行后面运算
        if self.model_device.startswith('cuda'):
            results.pred[0] = results.pred[0].cpu()

        names_index = {name: k for k, name in results.names.items()}

        logger.info(f'{cno}-predict_single_frame: found {len(results.pred[0])} objects: {[(results.names[int(p[-1])], p[-2]) for p in results.pred[0]]}')

        # 取得分类索引对应的阈值和roi区域
        thresholds = {names_index.get(ca['model_name']): ca['alert_threshold'] for ca in avail_cas}
        regions = {names_index.get(ca['model_name']): ca['roi_region'] for ca in avail_cas}

        # 过滤掉小于threshold或者不在roi_region的结果
        index = []
        class_indexes = []
        pred = results.pred[0].numpy()
        for i in range(pred.shape[0]):
            # 保留能识别并且阈值足够大的结果类别
            class_index = pred[i, -1]
            confidence = pred[i, -2]
            if class_index in thresholds and confidence >= thresholds[class_index] and self.pred_in_roi_region(regions[class_index], pred[i]):
                index.append(i)
                class_indexes.append(class_index)

        results.pred[0] = results.pred[0][index, :]

        pred = results.pred[0]
        if not pred.shape[0]:
            # 如果没有合适结果，直接返回
            return

        logger.info(f'{cno}-predict_single_frame: remain {len(results.pred[0])} objects: {[results.names[int(p[-1])] for p in results.pred[0]]}')

        # 首先保存未标注的图片
        img_unmark = save_raw_frame(results.ims[0], cno=cno, cvt_color=False)

        # 如果有多个类别被发现了，逐个保存，所以这里要先保存旧数据
        saved_img = results.ims[0].copy()
        saved_pred = results.pred[0]
        saved_class_indexes = list(set(class_indexes))  # 避免同一类目多次处理
        saved_regions = {**regions}

        for class_index in saved_class_indexes:
            class_indexes = [class_index]
            regions = {class_index: saved_regions[class_index]}
            results.ims[0] = saved_img.copy()
            results.pred[0] = saved_pred[saved_pred[:, -1] == class_index]
            pred = results.pred[0]

            self.addRoiRegion(results, regions, class_indexes)
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

            logger.info(f'{cno}-predicts: , {predicts}')

            # 保存报警信息
            ImageClient(IMG_CMD_OBJECT_DETECTED, cno=cno, img_unmark=img_unmark, img=img, predicts=predicts).do_request(wait_result=False)


class ImageConsumeThread(Thread):
    def __init__(self, process, model_path=None, model_device=None):
        super(ImageConsumeThread, self).__init__(target=self.process_loop)
        self.process = process
        self.cno = process.cno
        self.raw_img_queue = process.raw_img_queue
        # 分配一个足够大的buffer暂存最后一张图片
        self.model = DetectionModel(model_path, model_device, process.cas_queue)

    # 在缓冲栈中读取数据:
    def process_loop(self):
        logger.info(f'{self.cno}-Process to read: %s' % os.getpid())
        self.model.init_model()
        # 开始时间
        t1 = time.time()  # 最新图片保存定时
        t2 = time.time()  # 预测定时

        frame_count = 0
        while True:
            try:
                value = self.raw_img_queue.get_nowait()
            except Exception as e:  # Queue.Empty
                time.sleep(0.5)
                continue

            frame_count += 1

            if frame_count % 10 == 0:
                logger.info(f'{self.cno}-read frame_count: {frame_count}')

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

                self.process.save_latest_image(frame)
