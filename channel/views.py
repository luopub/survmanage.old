from django.shortcuts import render
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from cameradaemon.image_client import ImageClient
from cameradaemon.image_server_code import *
from utils.image_clear_thread import image_clear_thread

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

    @action(detail=False, methods=['post'])
    def config_alg_by_channel(self, request):
        alg_name = request.data.get('alg_name')
        status = request.data.get('status')
        self.model.config_alg_by_channel(alg_name, status)
        return Response({})

    @action(detail=True, methods=['post'])
    def config_single_alg(self, request, pk):
        channel = self.model.objects.get(pk=pk)
        alg_name = request.data.get('alg_name')
        status = request.data.get('status')
        channel.config_single_alg(alg_name, status)
        return Response({})

    @action(detail=False, methods=['get'])
    def get_real_time_status(self, request):
        channel_ids = request.GET.get('channel_ids').split(',')
        id_cnos = self.model.objects.filter(id__in=channel_ids).values_list('id', 'cno')
        status = {}
        for id_cno in id_cnos:
            id_ = id_cno[0]
            cno = id_cno[1]
            res = ImageClient(IMG_CMD_CHANNEL_GET_ONLINE, cno=cno).do_request()
            if res and res['code'] == IMG_CODE_SUCCESS:
                status[id_] = res['data']['online']
            else:
                status[id_] = False
        return Response(status)

    @action(detail=True, methods=['get'])
    def get_real_time_image(self, request, pk):
        channel = self.model.objects.get(id=pk)

        res = ImageClient(IMG_CMD_GET_LATEST_IMAGE, cno=channel.cno).do_request()
        if res and res['code'] == IMG_CODE_SUCCESS:
            image_clear_thread.put_image(res['data']['filename'])
            return Response({'filename': res['data']['filename']})
        else:
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
