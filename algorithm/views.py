from django.shortcuts import render
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase

from .models import Algorithm, AlgorithmDefaultParameters


class AlgorithmViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Algorithm


class AlgorithmParametersDefaultViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = AlgorithmDefaultParameters

    @action(detail=False, methods=['get'])
    def get_default(self, request):
        """
        由于取消了默认参数设置，这里返回固定值
        """
        value = [
            {
                "alert_interval": 30,
                "alert_threshold": 0.5,
                "alert_times": "[{\"enabled\":true,\"segs\":[[0,1440]]},{\"enabled\":true,\"segs\":[[0,1440]]},{\"enabled\":true,\"segs\":[[0,1440]]},{\"enabled\":true,\"segs\":[[0,1440]]},{\"enabled\":true,\"segs\":[[0,1440]]},{\"enabled\":true,\"segs\":[[0,1440]]},{\"enabled\":true,\"segs\":[[0,1440]]}]",
                "analyze_interval": 1000,
                "id": 10
            }
        ]
        return Response(value)


router = routers.DefaultRouter()
router.register('algorithms', AlgorithmViewSet)
router.register('algorithmdefaultparameters', AlgorithmParametersDefaultViewSet)
