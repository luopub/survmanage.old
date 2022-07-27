from django.shortcuts import render
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase

from .models import Alert


class AlertViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Alert

    @action(detail=False, methods=['get'])
    def get_real_time_image(self, request):
        alert_ids = request.GET.get('alert_ids').split(',')
        images = {id_: 'duiyaduiya-rt.png' for id_ in alert_ids}
        return Response(images)


class AlertViewSet2(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Alert

    serial_depth = 1


router = routers.DefaultRouter()
router.register('alerts', AlertViewSet)
router.register('alerts2', AlertViewSet2)
