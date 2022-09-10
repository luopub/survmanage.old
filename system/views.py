import platform
import os
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings
from rest_framework.authtoken.models import Token

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.error_code import ErrorCode
from utils.code_message_exception import CodeMsgException

from channel.models import Channel, ChannelAlgorithm
from algorithm.models import Algorithm, AlgorithmDefaultParameters
from alert.models import Alert

from .models import ProjectInfo

from . import deviceinfo


class ProjectInfoViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ProjectInfo

    authentication_classes = []
    permission_classes = []

    @action(detail=False, methods=['get'])
    def auth_info(self, request):
        if settings.AUTH_CHECK_ONLINE:
            code, message = self.model.re_activate()
            if code != 0:
                raise CodeMsgException(code, message)
        else:
            if self.model.objects.count() == 0:
                raise CodeMsgException('NOT_ACTIVATED', '系统尚未激活')

        return Response({'project_name': self.model.objects.first().project_name})

    @action(detail=False, methods=['post'])
    def activate(self, request):
        # if self.model.activated():
        #     raise CodeMsgException(ErrorCode.ALREADY_ACTIVED, '项目不能重复激活')

        # 检查项目名称
        data = request.data
        project_name = data.get('project_name')
        if not project_name:
            raise CodeMsgException(ErrorCode.INVALID_PROJECT_NAME, '项目名称无效')

        # auth_code = data.get('auth_code')
        # if not self.model.check_auth_code(auth_code):
        #     raise CodeMsgException(ErrorCode.INVALID_AUTH_CODE, '授权码无效或已使用')

        username = data.get('username')
        password = data.get('password')
        if not username:
            raise CodeMsgException(ErrorCode.INVALID_USERNAME, '用户名不能为空')
        if not password:
            raise CodeMsgException(ErrorCode.INVALID_PASSWORD, '密码不能为空')

        # 先新建用户
        try:
            # 如果用户名已经存在，删除后重新创建
            user = User.objects.get(username=username)
            Token.objects.filter(user=user).delete()
            user.delete()
        except Exception as e:
            pass
        try:
            user = User.objects.create_user(username=username, password=password)
        except Exception as e:
            raise CodeMsgException(ErrorCode.INVALID_USERNAME_OR_PASSWORD, '用户名或密码不合格')

        # Save after all check finished
        auth_code = data.get('auth_code')
        code, message = self.model.activate(project_name, auth_code)
        if code:
            # 如果激活失败，就将用户删除。以免产生多个用户
            user.delete()
            raise CodeMsgException(code, message)
        else:
            return Response({})

    @action(detail=False, methods=['get'])
    def get_disk_stats(self, request):
        """
        Return disk stats in GB
        """
        if settings.IS_DEPLOYED:
            s = os.statvfs('/')
            stats = {
                'size': s.f_bsize * s.f_blocks / (1 << 30),
                'free': s.f_bsize * s.f_bavail / (1 << 30)
            }
        else:
            stats = {'size': 1e3, 'free': 3.5e2}
        return Response(stats)

    @action(detail=False, methods=['get'])
    def get_device_info(self, request):
        di = {
            'memory': deviceinfo.memory_stat(),
            'cpu': deviceinfo.cpu_stat(),
            'load': deviceinfo.load_stat(),
            'uptime': deviceinfo.uptime_stat(),
            'net': deviceinfo.net_stat(),
            'disk': deviceinfo.disk_stat(),
            'release': deviceinfo.release_stat(),
            'host': deviceinfo.host_stat(),
            'uname': deviceinfo.uname_stat(),
        }
        return Response(di)

    @action(detail=False, methods=['post'])
    def start_upgrade(self, request):
        with open(settings.UPGRADE_FLAG_FILE, 'wt') as f:
            f.write('start upgrade')

        return Response({})

    @action(detail=False, methods=['post'])
    def reset_device(self, request):
        with open(settings.RESET_FLAG_FILE, 'wt') as f:
            f.write('start reset')

        return Response({})

    @action(detail=False, methods=['post'])
    def reset_params(self, request):
        ChannelAlgorithm.delete_all()
        AlgorithmDefaultParameters.delete_all()

        with open(settings.RESET_FLAG_FILE, 'wt') as f:
            f.write('start reset')

        return Response({})

    @staticmethod
    def delete_all_data():
        image_dir = settings.ALERT_IMAGE_DIR
        if platform.system().lower() == 'linux':
            del_cmd = f'rm -rf {image_dir}/*'
        else:
            del_cmd = rf'del /F/S/Q {image_dir}\*'

        os.system(del_cmd)

    @action(detail=False, methods=['post'])
    def factory_reset(self, request):
        Alert.delete_all()
        ChannelAlgorithm.delete_all()
        Channel.delete_all()
        Algorithm.delete_all()
        AlgorithmDefaultParameters.delete_all()
        ProjectInfo.delete_all()
        User.objects.all().delete()
        self.delete_all_data()

        with open(settings.RESET_FLAG_FILE, 'wt') as f:
            f.write('start reset')

        return Response({})


router = routers.DefaultRouter()
router.register('projectinfos', ProjectInfoViewSet)
