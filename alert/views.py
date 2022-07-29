from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters

from algorithm.models import Algorithm
from channel.models import Channel
from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.utils import get_filter_for_all_fields

from .models import Alert


class AlertViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Alert

    @action(detail=False, methods=['get'])
    def get_real_time_image(self, request):
        alert_ids = request.GET.get('alert_ids').split(',')
        images = {id_: 'duiyaduiya-rt.png' for id_ in alert_ids}
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
    model = Alert
    filterset_class = AlertViewFilter2

    serial_depth = 1


router = routers.DefaultRouter()
router.register('alerts', AlertViewSet)
router.register('alerts2', AlertViewSet2)
