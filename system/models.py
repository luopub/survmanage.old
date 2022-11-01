import requests
from django.db import models
from django.conf import settings
from algorithm.models import Algorithm

from utils.error_code import ErrorCode

MAX_PROJECT_NAME_LEN = 32
MAX_AUTH_CODE_LEN = 32

MAX_IMAGE_NAME_LEN = 64
MAX_IMAGE_FILE_LEN = 256


class ProjectInfo(models.Model):
    """
    ToDo:
        1. 是否需要二次激活（延期、增加算法等）
        2. auth_code需要与authserver联动
    """
    project_name = models.CharField(max_length=MAX_PROJECT_NAME_LEN, verbose_name='项目名称')
    auth_code = models.CharField(max_length=MAX_AUTH_CODE_LEN, unique=True, verbose_name='授权码')
    verification_code = models.CharField(max_length=MAX_AUTH_CODE_LEN, null=True, verbose_name='激活码')  # 证明是同一个人激活

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()

    # @classmethod
    # def activated(cls):
    #     return cls.objects.count() > 0 and cls.objects.first().verification_code

    @classmethod
    def re_activate(cls):
        """
        使用当前验证信息重新获取激活信息
        """
        obj = cls.objects.first()
        if obj:
            return cls.activate(obj.project_name, obj.auth_code, verification_code=obj.verification_code)
        else:
            return ErrorCode.NOT_ACTIVATED, '尚未激活'

    @classmethod
    def activate(cls, project_name, auth_code, verification_code=None):
        # 如果已经有激活信息，那么再次验证
        # if obj:
        #     verification_code = obj.verification_code
        # else:
        #     verification_code = None

        r = requests.post(settings.AUTH_SERVER_ROOT + 'authorizer/authorizations/activate/',
                          json={'auth_code': auth_code, 'verification_code': verification_code})
        r = r.json()
        if r['code'] != 0:
            return r['code'], r['message']

        obj = cls.objects.first()
        if not obj:
            obj = cls()
            # Save algorithms. If we are a new auth code, delete the old algorithms.
            Algorithm.refresh(r['data']['algorithms'], delete_old=True)
        else:
            # Save algorithms
            Algorithm.refresh(r['data']['algorithms'], delete_old=True)

        verification_code = r['data']['verification_code']
        # 如果没有变化就不用保存
        if obj.project_name != project_name or obj.auth_code != auth_code or obj.verification_code != verification_code:
            obj.project_name = project_name
            obj.auth_code = auth_code
            obj.verification_code = verification_code
            obj.save()

        return 0, 'Success'

    @classmethod
    def check_auth_code(cls, auth_code):
        if not auth_code or len(auth_code) != MAX_AUTH_CODE_LEN or cls.objects.filter(auth_code=auth_code).count() > 0:
            return False
        return True


class ImageIcon(models.Model):
    """
    保存算法和系统图片、图表
    """
    name = models.CharField(max_length=MAX_IMAGE_NAME_LEN, unique=True, verbose_name='图片/图标名称')
    file_name = models.CharField(max_length=MAX_IMAGE_FILE_LEN, verbose_name='文件名称, 可以在/static/images获取')
