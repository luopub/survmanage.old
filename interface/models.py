from django.db import models
from django.conf import settings
import requests

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


class BenzhiProvider(models.Model):
    provider_name = models.CharField(max_length=MAX_PROVIDER_NAME_LEN, unique=True, verbose_name='ProviderName')


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


class BenzhiEventToAlgorithm(models.Model):
    event_type = models.CharField(max_length=MAX_EVENT_TYPE_LEN)
    algorithm = models.CharField(max_length=MAX_ALGORITHM_NAME_LEN)

    class Meta:
        unique_together = (('event_type', 'algorithm'),)


class BenzhiMetadata(models.Model):
    key = models.CharField(max_length=MAX_KEY_LEN, unique=True)
    value = models.CharField(max_length=MAX_VALUE_LEN)


class BenzhiReportUrl(models.Model):
    url = models.URLField(unique=True)

    @classmethod
    def send_alert(cls, alert):
        try:
            if not BenzhiSubscription.objects.get(algorithm=alert.algorithm).is_subscribed:
                return

            if cls.objects.all().count() == 0:
                return

            dt = datetime_utc_to_local(alert.date_time)
            data = {
                'eventId': alert.id,
                'cameraId': alert.channel.cid,
                'cameraId_url': alert.channel.url,
                'alertTime_begin': dt.strftime('%Y-%m-%d %H:%M:%S'),
                'alertTime_end': dt.strftime('%Y-%m-%d %H:%M:%S'),
                'alertPic_URL': None,
                'alertPic_base64': image_to_data_url(settings.ALERT_IMAGE_DIR.joinpath(alert.img)),
                'eventTypeCode': alert.algorithm.event_type,
                'eventTypeName': alert.algorithm.name_ch,
                'eventLevelName': None,
                'eventLocation': alert.channel.site
            }

            headers = {}
            for obj in BenzhiMetadata.objects.all():
                headers[obj.key] = obj.value

            for obj in cls.objects.all():
                requests.post(obj.url, json=data, timeout=10, headers=headers)
        except Exception as e:
            logger.info(f'Error sending alert report: {str(e)}')
            pass


Alert.add_post_save_handler(BenzhiReportUrl.send_alert)
