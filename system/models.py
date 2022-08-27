import requests
from django.db import models
from django.conf import settings
from algorithm.models import Algorithm

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
    verification_code = models.CharField(max_length=MAX_AUTH_CODE_LEN, null=True, verbose_name='激活码')  # 证明是同一个人激活

    @classmethod
    def activated(cls):
        return cls.objects.count() > 0 and cls.objects.first().verification_code

    @classmethod
    def activate(cls, project_name, auth_code):
        # if cls.activated():
        #     return False
        # cls(name=project_name, auth_code=auth_code).save()

        # 如果已经有激活信息，那么再次验证
        obj = cls.objects.first()
        if obj:
            verification_code = obj.verification_code
        else:
            verification_code = None

        r = requests.post(settings.AUTH_SERVER_ROOT + 'authorizer/authorizations/activate/',
                          json={'auth_code': auth_code, 'verification_code': verification_code})
        r = r.json()
        if r['code'] != 0:
            return r['code'], r['message']

        if not obj:
            obj = cls()

        verification_code = r['data']['verification_code']
        # 如果没有变化就不用保存
        if obj.name != project_name or obj.auth_code != auth_code or obj.verification_code != verification_code:
            obj.name = project_name
            obj.auth_code = auth_code
            obj.verification_code = verification_code
            obj.save()

        # Save algorithms
        Algorithm.refresh(r['data']['algorithms'])

        return 0, 'Success'

    @classmethod
    def check_auth_code(cls, auth_code):
        if not auth_code or len(auth_code) != MAX_AUTH_CODE_LEN or cls.objects.filter(auth_code=auth_code).count() > 0:
            return False
        return True
