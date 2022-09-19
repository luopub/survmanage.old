from django.db import models
from django.utils import timezone

from algorithm.models import MAX_ALGORITHM_NAME_LEN, Algorithm

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
