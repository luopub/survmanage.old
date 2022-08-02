import time
import os
import ctypes
import json
from django.conf import settings

from channel.models import Channel

from .image_read_process import ImageStreamProcess, ImageConsumeProcess
from .image_server import ImageServer
from .image_server_code import *
from .utils import save_raw_frame


class ImageProcessPair:
    def __init__(self, cno, camera):
        self.cno = cno
        self.camera = camera
        self.raw_img_queue = None
        self.pw = None
        self.pr = None

    def start(self):
        # pw = Process(target=write, args=(q, rtsp_url, queue_size))
        self.pw = ImageStreamProcess(self.camera)
        self.pr = ImageConsumeProcess(self.cno, self.pw.raw_img_queue, model_path=settings.MODEL_PATH, model_device=settings.MODEL_DEVICE)
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

    def get_latest_image(self, cno):
        frame = self.process_pairs[cno - 1].pr.get_latest_image()

        return save_raw_frame(frame, cno=cno)

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
            data = json.loads(data.decode('utf8'))
            cmd = data['cmd']
            if cmd == IMG_CMD_GET_LATEST_IMAGE:
                cno = data['data']['cno']
                res = {
                    'code': IMG_CODE_SUCCESS,
                    'data': {
                        'filename': self.get_latest_image(cno)
                    }
                }
        except:
            pass
        return json.dumps(res).encode('utf8')

    def main_loop(self):
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
