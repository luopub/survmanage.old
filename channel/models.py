import json
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from algorithm.models import Algorithm, AlgorithmParametersBase

from utils.utils import values_list_to_list
from cameradaemon.image_client import ImageClient
from cameradaemon.image_server_code import *

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

    def config_alg(self, data):
        """
        Configure algorithm for this channel
        """
        for k, v in data.items():
            if not v['configured'] or v['configured'] == '0':
                try:
                    self.channelalgorithm_set.get(algorithm__name=k).delete()
                except ChannelAlgorithm.DoesNotExist as e:
                    pass
            else:
                algorithm = Algorithm.objects.get(name=k)
                ChannelAlgorithm.objects.update_or_create(channel=self, algorithm=algorithm, defaults={
                    'analyze_interval': v.get('analyze_interval'),
                    'alert_interval': v.get('alert_interval'),
                    'alert_threshold': v.get('alert_threshold'),
                    'alert_times': v.get('alert_times'),
                    'roi_region': v.get('roi_region')
                })
        # 通知后台程序
        ImageClient(IMG_CMD_CHANNEL_ALG_CHANGED, cno=self.cno).do_request(wait_result=False)


@receiver(post_save, sender=Channel)
def on_channel_post_save(sender, **kwargs):
    ImageClient(IMG_CMD_CHANNEL_CONFIGURED, cno=kwargs['instance'].cno).do_request(wait_result=False)


class ChannelAlgorithm(AlgorithmParametersBase):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name='通道')
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE, verbose_name='算法')
    # json format boxes list
    roi_region = models.CharField(max_length=1024, null=True, verbose_name='ROI矩形区')

    class Meta:
        unique_together = (('channel', 'algorithm'),)

    @staticmethod
    def decode_roi(roi_region):
        if not roi_region:
            left = top = width = height = 0
        else:
            values = roi_region.split(',')
            left = int(values[0])
            top = int(values[1])
            width = int(values[2])
            height = int(values[3])

        return left, top, width, height

    @staticmethod
    def encode_roi(left, top, width, height):
        return f'{left},{top},{width},{height}'

    @classmethod
    def get_cas_params(cls, cno):
        cas = list(cls.objects.filter(channel__cno=cno).values(
            'channel__cno',
            'algorithm__name',
            'analyze_interval',
            'alert_interval',
            'alert_threshold',
            'alert_times',
        ))

        new_cas = []
        for ca in cas:
            # 将算法名称映射成模型支持的名称，如果是模型不支持的算法，就忽略掉
            model_name = Algorithm.map_alg_name_to_model_name(ca['algorithm__name'])
            if not model_name:
                continue

            ca['model_name'] = model_name

            # 将alert_times解码
            if ca['alert_times']:
                ca['alert_times'] = json.loads(ca['alert_times'])

            new_cas.append(ca)

        return new_cas

