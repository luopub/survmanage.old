from django.db import models


MAX_PROJECT_NAME_LEN = 32
MAX_AUTH_CODE_LEN = 32


class ProjectInfo(models.Model):
    name = models.CharField(max_length=MAX_PROJECT_NAME_LEN, verbose_name='项目名称')
    auth_code = models.CharField(max_length=MAX_AUTH_CODE_LEN, unique=True, verbose_name='授权码')
