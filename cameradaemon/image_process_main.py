import time
import os
import ctypes
import json
from django.conf import settings

from algorithm.models import Algorithm
from channel.models import Channel, ChannelAlgorithm
from alert.models import Alert

from .image_read_process import ImageStreamProcess, ImageConsumeProcess
from .image_server import ImageServer
from .image_server_code import *
from .utils import save_raw_frame

from utils.logutils import get_logger
logger = get_logger(__file__)


class ImageProcessPair:
    def __init__(self, cno, camera):
        self.cno = cno
        self.camera = camera
        self.raw_img_queue = None
        self.pw = ImageStreamProcess(self.camera, self.cno)
        self.pr = ImageConsumeProcess(self.cno, self.pw.raw_img_queue, model_path=settings.MODEL_PATH, model_device=settings.MODEL_DEVICE)

    def start(self):
        # pw = Process(target=write, args=(q, rtsp_url, queue_size))
        # 启动子进程pw，写入:
        self.pw.start()
        # 启动子进程pr，读取:
        self.pr.start()


class ImageChannelsManager:
    def __init__(self, channels_num):
        # 通道编号转换成索引
        self.channels_num = channels_num
        self.process_pairs = [ImageProcessPair(c+1, '') for c in range(self.channels_num)]
        # super(ImageChannelsManager, self).__init__(target=self.process_loop)

    def config_channels(self):
        for pp in self.process_pairs:
            cas = ChannelAlgorithm.get_cas_params(pp.cno)
            pp.pr.set_params(cas)

    def start_channels(self):
        for pp in self.process_pairs:
            pp.start()

    def set_channel_camera(self, cno, camera):
        """
        :param cno: channel number - 1 = index
        :param camera: camera is the rtsp url
        :return:
        """
        if cno > len(self.process_pairs):
            return False
        self.process_pairs[cno - 1].pw.change_camera(camera)
        return True

    def set_channel_algorithms(self):
        pass

    def get_latest_image(self, pp):
        frame = pp.pr.get_latest_image()

        return save_raw_frame(frame, cno=pp.cno)

    def get_pp_from_cmd(self, data):
        """
        Get cno and pp and result if not valid cno
        """
        cno = data['data']['cno']
        pps = list(filter(lambda x: x.cno == cno, self.process_pairs))
        res = None
        if pps:
            pp = pps[0]
        else:
            res = {
                'code': IMG_CODE_CHANNEL_NOT_FOUND,
                'data': {}
            }
        return cno, pp, res

    def handlers(self, data):
        """
        所有命令应该是json格式:
        {
            cmd: int,
            data: dict
        }
        返回值：
        {
            code: int,
            data: dict
        }
        成功返回code=0
        """
        if not data:
            return None

        res = {
            'code': IMG_CODE_INVALID_CMD,
            'data': {}
        }
        try:
            cmd = data['cmd']
            if cmd == IMG_CMD_OBJECT_DETECTED:
                cno = data['data']['cno']
                img = data['data']['img']
                img_unmark = data['data']['img_unmark']
                predicts = data['data']['predicts']
                alert_ids = Alert.add_alerts(cno=cno, img_unmark=img_unmark, img=img, predicts=predicts)
                logger.info(f'new alerts added: {alert_ids}')
                res = {
                    'code': IMG_CODE_SUCCESS,
                    'data': {}
                }
            elif cmd == IMG_CMD_GET_LATEST_IMAGE:
                cno, pp, res = self.get_pp_from_cmd(data)
                if pp:
                    res = {
                        'code': IMG_CODE_SUCCESS,
                        'data': {
                            'filename': self.get_latest_image(pp)
                        }
                    }
            elif cmd == IMG_CMD_CHANNEL_ALG_CHANGED:
                cno, pp, res = self.get_pp_from_cmd(data)
                if pp:
                    cas = ChannelAlgorithm.get_cas_params(pp.cno)
                    pp.pr.set_params(cas)
                    res = {
                        'code': IMG_CODE_SUCCESS,
                        'data': {}
                    }
            elif cmd == IMG_CMD_CHANNEL_CONFIGURED:
                cno, pp, res = self.get_pp_from_cmd(data)
                if pp:
                    try:
                        channel = Channel.objects.get(cno=cno)
                        pp.pw.change_camera(channel.url)
                        res = {
                            'code': IMG_CODE_SUCCESS,
                            'data': {}
                        }
                    except Channel.DoesNotExist:
                        res = {
                            'code': IMG_CODE_CHANNEL_NOT_FOUND,
                            'data': {}
                        }
            elif cmd == IMG_CMD_CHANNEL_DELETED:
                cno, pp, res = self.get_pp_from_cmd(data)
                if pp:
                    pp.pw.change_camera('')
                    res = {
                        'code': IMG_CODE_SUCCESS,
                        'data': {}
                    }
            elif cmd == IMG_CMD_CHANNEL_GET_ONLINE:
                cno, pp, res = self.get_pp_from_cmd(data)
                if pp:
                    res = {
                        'code': IMG_CODE_SUCCESS,
                        'data': {'online': not not pp.pw.online.value}
                    }
        except:
            pass
        return res

    def main_loop(self):
        self.config_channels()

        self.start_channels()

        time.sleep(5)

        # 读取通道数据，设置camera地址
        channels = Channel.objects.all()
        for c in channels:
            if c.cno > self.channels_num:
                continue
            self.set_channel_camera(c.cno, c.url)

        ImageServer.serve(self.handlers)
        # while True:
        #     time.sleep(1)

    @staticmethod
    def main(**kwargs):
        max_camera = int(kwargs.get('max_camera', '2'))

        rtsp_url = 'rtsp://admin:qwer123456@192.168.0.6:554/h264/ch1/main/av_stream'

        icm = ImageChannelsManager(max_camera)

        icm.main_loop()
