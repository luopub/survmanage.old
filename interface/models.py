from django.db import models
from django.conf import settings
import requests
import json

from algorithm.models import MAX_ALGORITHM_NAME_LEN, Algorithm
from alert.models import Alert
from utils.datetime_utils import datetime_utc_to_local
from utils.utils import image_to_data_url

from utils.logutils import get_logger
logger = get_logger('interface_models')

MAX_EVENT_TYPE_LEN = 32
MAX_EVENT_TYPE_NAME_LEN = 32
MAX_PROVIDER_NAME_LEN = 32
MAX_KEY_LEN = 32
MAX_VALUE_LEN = 32
MAX_REPORT_META_LEN = 2048


class BenzhiSubscription(models.Model):
    algorithm = models.OneToOneField(Algorithm, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=True)

    @classmethod
    def on_activated(cls):
        """
        On activation, enable all algorithms to be subscribed
        """
        # Delete all, then add again
        cls.objects.all().delete()

        for obj in Algorithm.objects.all():
            cls.objects.update_or_create(algorithm=obj, is_subscribed=True)


Algorithm.add_activation_handler(BenzhiSubscription.on_activated)


class BenzhiReportUrl(models.Model):
    url = models.URLField(unique=True, verbose_name='URL to Report Alert')
    platform_name = models.CharField(max_length=MAX_PROVIDER_NAME_LEN, default='本质', verbose_name='Report Platform Name')
    provider_name = models.CharField(max_length=MAX_PROVIDER_NAME_LEN, default='美云数字', verbose_name='ProviderName')
    enabled = models.BooleanField(default=True, verbose_name='Report Enabled')
    metadata = models.CharField(max_length=MAX_REPORT_META_LEN, null=True, verbose_name='Metadata (key, value) pairs in JSON format')

    @classmethod
    def send_alert(cls, alert):
        try:
            if not BenzhiSubscription.objects.get(algorithm=alert.algorithm).is_subscribed:
                return

            for obj in cls.objects.filter(enabled=True):

                dt = datetime_utc_to_local(alert.date_time)
                data = {
                    'eventId': alert.id,
                    'cameraId': alert.channel.cid,
                    'cameraId_url': alert.channel.url,
                    'alertTime_begin': dt.strftime('%Y-%m-%d %H:%M:%S'),
                    'alertTime_end': dt.strftime('%Y-%m-%d %H:%M:%S'),
                    'alertPic_URL': None,
                    'alertPic_base64': image_to_data_url(settings.ALERT_IMAGE_DIR.joinpath(alert.img)),
                    'eventTypeCode': alert.algorithm.name,
                    'eventTypeName': alert.algorithm.name_ch,
                    'eventLevelName': '低',
                    'enventLocation': alert.channel.site  # event was wrong to envent
                }

                if obj.metadata:
                    headers = json.loads(obj.metadata)
                else:
                    headers = {}

                # logger.info(f'Reporting to benzhi: {json.dumps(data, indent=2, ensure_ascii=False)}')
                res = requests.post(obj.url, json=data, timeout=10, headers=headers)
                if res.status_code == 200:
                    logger.info(f'Save to benzhi success: {res.json()}')
                else:
                    logger.info(f'Send to benzhi failed: {res.status_code}, {res.test}')
        except Exception as e:
            logger.info(f'Error sending alert report: {str(e)}')
            pass


Alert.add_post_save_handler(BenzhiReportUrl.send_alert)
