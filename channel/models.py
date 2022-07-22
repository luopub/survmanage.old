from django.db import models

from algorithm.models import Algorithm, AlgorithmParametersMixin

from utils.utils import values_list_to_list

MAX_CHANNEL_NUM = 8

MAX_CHANNEL_ID_LEN = 32
MAX_CHANNEL_NAME_LEN = 64
MAX_CHANNEL_SITE_LEN = 64
MAX_CHANNEL_URL_LEN = 1024


class Channel(models.Model):
    cno = models.IntegerField(unique=True, verbose_name='通道编号')
    cid = models.CharField(max_length=MAX_CHANNEL_ID_LEN, unique=True, verbose_name='通道ID')
    name = models.CharField(max_length=MAX_CHANNEL_NAME_LEN, verbose_name='通道名称')
    site = models.CharField(max_length=MAX_CHANNEL_SITE_LEN, verbose_name='通道位置')
    url = models.CharField(max_length=MAX_CHANNEL_URL_LEN, verbose_name='通道RTSP网址')

    @classmethod
    def get_used_free_channel_nos(cls):
        used_nos = values_list_to_list(cls.objects.all().values_list('cno'))
        free_nos = [n for n in range(1, MAX_CHANNEL_NUM+1) if n not in used_nos]
        return used_nos, free_nos


class ChannelAlgorithm(models.Model, AlgorithmParametersMixin):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name='通道')
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE, verbose_name='算法')
    # Comma seperated integers left, top, width, height
    poi_rect = models.CharField(max_length=20, null=True, verbose_name='POI矩形区')

    @staticmethod
    def decode_poi(poi_rect):
        if not poi_rect:
            left = top = width = height = 0
        else:
            values = poi_rect.split(',')
            left = int(values[0])
            top = int(values[1])
            width = int(values[2])
            height = int(values[3])

        return left, top, width, height

    @staticmethod
    def encode_poi(left, top, width, height):
        return f'{left},{top},{width},{height}'
