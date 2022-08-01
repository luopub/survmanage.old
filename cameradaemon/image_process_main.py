import cv2 as cv
import numpy as np
from PIL import Image
import time
import os
import ctypes
import json
import hashlib
from django.conf import settings

from multiprocessing import Process, Queue, Manager

from channel.models import Channel

from .image_read_process import ImageProcessPair
from .image_server import ImageServer
from .image_server_code import *


class ImageChannelsManager:
    def __init__(self, channels_num):
        # 通道编号转换成索引
        self.channels_num = channels_num
        self.process_pairs = [ImageProcessPair('') for _ in range(self.channels_num)]
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

    def save_image_file(self, raw_frame):
        # 格式转变，BGRtoRGB
        frame = cv.cvtColor(raw_frame, cv.COLOR_BGR2RGB)

        md5 = hashlib.md5()
        md5.update(frame.tobytes())
        digest = md5.hexdigest()

        # 转变成Image
        image = Image.fromarray(np.uint8(frame))

        filename = f'{digest}.jpg'

        filepath = settings.ALERT_IMAGE_DIR.joinpath(filename)

        image.save(filepath)

        return filename

    def get_latest_image(self, cno):
        frame = self.process_pairs[cno - 1].pr.get_latest_image()

        return self.save_image_file(frame)

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
        res = {
            'code': CODE_INVALID_CMD,
            'data': {}
        }
        try:
            data = json.loads(data.decode('utf8'))
            cmd = data['cmd']
            if cmd == CMD_GET_LATEST_IMAGE:
                cno = data['data']['cno']
                res = {
                    'code': CODE_SUCCESS,
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
