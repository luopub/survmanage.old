from django.db import models
from django.utils import timezone

from algorithm.models import MAX_ALGORITHM_NAME_LEN

MAX_EVENT_TYPE_LEN = 32
MAX_EVENT_TYPE_NAME_LEN = 32
MAX_PROVIDER_NAME_LEN = 32
MAX_KEY_LEN = 32
MAX_VALUE_LEN = 32


class BenzhiProvider(models.Model):
    provider_name = models.CharField(max_length=MAX_PROVIDER_NAME_LEN, unique=True)


class BenzhiSubscription(models.Model):
    event_type = models.CharField(max_length=MAX_EVENT_TYPE_LEN, unique=True)
    event_type_name = models.CharField(max_length=MAX_EVENT_TYPE_NAME_LEN, unique=True)
    is_subscribed = models.BooleanField(default=True)
    subscribe_time = models.DateTimeField(default=timezone.now)
    unsubscribe_time = models.DateTimeField(null=True)


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
