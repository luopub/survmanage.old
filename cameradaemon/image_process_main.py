import cv2 as cv
import numpy as np
from PIL import Image
import time
import os
import ctypes

from multiprocessing import Process, Queue, Manager

from .image_read_process import ImageProcessPair


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

    def get_latest_image(self, cno):
        return self.process_pairs[cno - 1].pr.get_latest_image()

    def main_loop(self):
        self.start_channels()

        while True:
            time.sleep(1)

    @staticmethod
    def main(**kwargs):
        max_camera = int(kwargs.get('max_camera', '2'))

        rtsp_url = 'rtsp://admin:qwer123456@192.168.0.6:554/h264/ch1/main/av_stream'

        icm = ImageChannelsManager(max_camera)

        icm.main_loop()

        # for i in range(len(icm.process_pairs)):
        #     icm.set_channel_camera(i + 1, rtsp_url)

        # icm.join()

        # print('done')
