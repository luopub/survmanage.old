from django.shortcuts import render
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase

from .models import Channel, ChannelAlgorithm


class ChannelViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Channel

    @action(detail=False, methods=['get'])
    def get_used_free_channel_nos(self, request):
        used_nos, free_nos = self.model.get_used_free_channel_nos()
        return Response({'used_nos': used_nos, 'free_nos': free_nos})

    @action(detail=True, methods=['post'])
    def config_alg(self, request, pk):
        channel = self.model.objects.get(pk=pk)
        channel.config_alg(request.data)
        return Response({})


class ChannelAlgorithmViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ChannelAlgorithm


class ChannelAlgorithmViewSet2(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ChannelAlgorithm

    serial_depth = 1


router = routers.DefaultRouter()
router.register('channels', ChannelViewSet)
router.register('channelalgorithms', ChannelAlgorithmViewSet)
router.register('channelalgorithms2', ChannelAlgorithmViewSet2)
