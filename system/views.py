import os
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.error_code import ErrorCode
from utils.code_message_exception import CodeMsgException

from .models import ProjectInfo


class ProjectInfoViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ProjectInfo

    authentication_classes = []
    permission_classes = []

    @action(detail=False, methods=['get'])
    def auth_info(self, request):
        code, message = self.model.re_activate()
        if code != 0:
            raise CodeMsgException(code, message)

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
            User.objects.filter(username=username).delete()
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


router = routers.DefaultRouter()
router.register('projectinfos', ProjectInfoViewSet)
