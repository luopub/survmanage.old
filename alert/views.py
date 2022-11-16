import tempfile
import zipfile
import json
import os
from django.conf import settings
from django.http import FileResponse
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.db.models.functions.datetime import TruncHour, TruncDay
from django.db import connection

from algorithm.models import Algorithm
from channel.models import Channel
from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.utils import get_filter_for_all_fields
from utils.code_message_exception import CodeMsgException
from utils.error_code import ErrorCode
from utils.docker_utils import run_host_cmd

from cameradaemon.image_client import ImageClient
from cameradaemon.image_server_code import *
from utils.image_clear_thread import image_clear_thread
from utils.check_runserver import is_runserver

from .models import Alert

from utils.logutils import get_logger

logger = get_logger(__file__)


class AlertViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Alert

    @action(detail=False, methods=['get'])
    def get_real_time_image(self, request):
        alert_ids = request.GET.get('alert_ids').split(',')
        if not alert_ids:
            alert_ids = []
        else:
            alert_ids = [int(id_) for id_ in alert_ids]

        # 取得所有channel no，不用重复读取图片
        alert_channels = self.model.objects.filter(id__in=alert_ids).values_list('id', 'channel__cno')
        cnos = set([item[1] for item in alert_channels])
        cno_images = {}
        for cno in cnos:
            res = ImageClient(IMG_CMD_GET_LATEST_IMAGE, cno=cno).do_request()
            if res and res['code'] == IMG_CODE_SUCCESS:
                cno_images[cno] = res['data']['filename']
                image_clear_thread.put_image(res['data']['filename'])

        # 将图片与alert id对应
        images = {}
        for item in alert_channels:
            if item[1] in cno_images:
                images[str(item[0])] = cno_images[item[1]]

        # images = {id_: 'duiyaduiya-rt.png' for id_ in alert_ids}
        return Response(images)

    @action(detail=False, methods=['post'])
    def delete_mult(self, request):
        ids = request.data.get('ids', [])
        self.model.objects.filter(id__in=ids).delete()
        return Response({})

    def create_zip_file_from_qs(self, queryset):

        serializer = self.get_serializer(queryset, many=True)

        # first put everything in as single zipfile
        temp_zip_file = tempfile.mktemp(prefix='alerts-', suffix='.zip')

        zip = zipfile.ZipFile(temp_zip_file, mode='w')

        zip.writestr('alert-list.json', json.dumps(serializer.data))

        for obj in queryset:
            for img in [obj.img, obj.img_unmark]:
                try:
                    filepath = settings.ALERT_IMAGE_DIR.joinpath(img)
                    zip.write(filepath, arcname=os.path.join('images', filepath.name))
                except Exception as e:
                    pass

        zip.close()

        return temp_zip_file

    @staticmethod
    def get_file_download_response(filepath):
        file = open(filepath, 'rb')
        response = FileResponse(file, filename=filepath)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment;filename ="{os.path.basename(filepath)}"'

        return response

    @action(detail=False, methods=['get'])
    def download(self, request):
        filepath = request.GET.get('filepath')
        if filepath:
            return self.get_file_download_response(filepath)
        raise CodeMsgException(ErrorCode.INVALID_PARAMETERS, '参数不正确')

    @action(detail=False, methods=['get'])
    def download_selected(self, request):
        ids = [int(_id) for _id in request.GET.get('ids', '').split(',') if _id]

        queryset = self.model.objects.filter(id__in=ids)

        temp_zip_file = self.create_zip_file_from_qs(queryset)

        return Response({'filepath': temp_zip_file})

    @action(detail=False, methods=['get'])
    def download_filtered(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        temp_zip_file = self.create_zip_file_from_qs(queryset)

        return Response({'filepath': temp_zip_file})

    @action(detail=False, methods=['post'])
    def remove_all(self, request):
        # 首先删除数据库相关数据
        with connection.cursor() as cursor:
            cursor.execute("delete from django_migrations where app = 'alert';")
            cursor.execute("drop table if exists alert_alert;")

        # 然后删除所有文件
        image_paths = settings.ALERT_IMAGE_DIR.glob("*.jpg")
        for image in image_paths:
            image.unlink()

        # 最后重启系统
        if settings.IS_DEPLOYED:
            run_host_cmd('cd /docker && docker compose restart')
        return Response({})


class AlertViewFilter2(filters.FilterSet):
    class Meta:
        fields = get_filter_for_all_fields(Alert)
        channel_fields = get_filter_for_all_fields(Channel)
        channel_fields = {f'channel__{k}': v for k, v in channel_fields.items()}
        algorithm_fields = get_filter_for_all_fields(Algorithm)
        algorithm_fields = {f'algorithm__{k}': v for k, v in algorithm_fields.items()}
        fields.update(channel_fields)
        fields.update(algorithm_fields)
        model = Alert


class AlertViewSet2(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    logger.debug(f'is_runserver {is_runserver()}')
    if is_runserver():
        queryset = Alert.objects.all().annotate(
            hour=TruncHour('date_time'),
            day=TruncDay('date_time')
        )
    model = Alert
    filterset_class = AlertViewFilter2

    serial_depth = 1


router = routers.DefaultRouter()
router.register('alerts', AlertViewSet)
router.register('alerts2', AlertViewSet2)
