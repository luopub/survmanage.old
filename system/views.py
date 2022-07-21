from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.error_code import ErrorCode
from utils.code_message_exception import CodeMsgException

from .models import ProjectInfo


class ProjectInfoViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ProjectInfo

    @action(detail=False, methods=['get'])
    def activated(self, request):
        return Response({'activated': self.model.activated()})

    @action(detail=False, methods=['post'])
    def activate(self, request):
        if self.model.activated():
            raise CodeMsgException(ErrorCode.ALREADY_ACTIVED, '项目不能重复激活')

        data = request.data
        project_name = data.get('project_name')
        if not project_name:
            raise CodeMsgException(ErrorCode.INVALID_PROJECT_NAME, '项目名称无效')
        auth_code = data.get('auth_code')
        if not self.model.check_auth_code(auth_code):
            raise CodeMsgException(ErrorCode.INVALID_AUTH_CODE, '授权码无效或已使用')

        username = data.get('username')
        password = data.get('password')
        if not username:
            raise CodeMsgException(ErrorCode.INVALID_USERNAME, '用户名不能为空')
        if User.objects.filter(username=username).count() > 0:
            raise CodeMsgException(ErrorCode.INVALID_USERNAME, '用户名已经存在')
        if not password:
            raise CodeMsgException(ErrorCode.INVALID_PASSWORD, '密码不能为空')

        # Save after all check finished
        self.model.activate(project_name, auth_code)
        user = User.objects.create_user(username=username, password=password)

        return Response({})


router = routers.DefaultRouter()
router.register('projectinfos', ProjectInfoViewSet)
