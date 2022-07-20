from django.db import models


MAX_PROJECT_NAME_LEN = 32
MAX_AUTH_CODE_LEN = 32


class ProjectInfo(models.Model):
    """
    ToDo:
        1. 是否需要二次激活（延期、增加算法等）
        2. auth_code需要与authserver联动
    """
    name = models.CharField(max_length=MAX_PROJECT_NAME_LEN, verbose_name='项目名称')
    auth_code = models.CharField(max_length=MAX_AUTH_CODE_LEN, unique=True, verbose_name='授权码')

    @classmethod
    def activated(cls):
        return cls.objects.count() > 0

    @classmethod
    def activate(cls, project_name, auth_code):
        if cls.activated():
            return False
        cls(name=project_name, auth_code=auth_code).save()
        return True

    @classmethod
    def check_auth_code(cls, auth_code):
        if not auth_code or len(auth_code) != MAX_AUTH_CODE_LEN or cls.objects.filter(auth_code=auth_code).count() > 0:
            return False
        return True
