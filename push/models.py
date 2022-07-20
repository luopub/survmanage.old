from django.db import models


MAX_PUSH_URL_LEN = 1024


class Push(models.Model):
    push_enabled = models.BooleanField(default=True, verbose_name='是否开启推送')
    address = models.CharField(max_length=15, verbose_name='设备地址')


class PushUrl(models.Model):
    base64 = models.BooleanField(default=True, verbose_name='Base64编码')
    url = models.CharField(max_length=MAX_PUSH_URL_LEN, verbose_name='推送地址')
