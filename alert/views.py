from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.db.models.functions.datetime import TruncHour, TruncDay

from algorithm.models import Algorithm
from channel.models import Channel
from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.utils import get_filter_for_all_fields

from cameradaemon.image_client import ImageClient
from cameradaemon.image_server_code import *
from utils.image_clear_thread import image_clear_thread

from .models import Alert


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
