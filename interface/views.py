from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase

from channel.models import Channel, ChannelAlgorithm
from system.models import ProjectInfo

from .models import *


class BenzhiProviderViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = BenzhiProvider


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class BenzhiSubscriptionViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = BenzhiSubscription

    authentication_classes = []
    permission_classes = []

    @action(detail=False, methods=['get', 'post'])
    def get_subscription_types(self, request):
        provider_name = BenzhiProvider.objects.first().provider_name
        subscptions = self.model.objects.all().values('algorithm__event_type', 'algorithm__name_ch', 'is_subscribed')
        subscptions = list(map(lambda x: {
            'EventType': x['algorithm__event_type'],
            'EventTypeName': x['algorithm__name_ch'],
            'IsSubscribed': x['is_subscribed']
        }, subscptions))
        return Response({'ProviderName': provider_name, 'list': subscptions})

    @action(detail=False, methods=['post'])
    def get_subscription_cameras(self, request):
        """
        {
            "code": "0",
            "msg": "",
            "data": {
                ProviderName: "商提供名，如海康、极视角等"
                "list": [
                    {
                        "cameraId": "18ba2dc7c90e43cd93c5fa2ca834b193",
                        "name": "南中高速 TJ6 标-K19+017.000（枪机）",
                        "installLocation": "南中高速 TJ6 标-K19+017.000 物料后场出入口（枪机）",
                        "longitude": "113.450839",
                        "latitude": "22.585688",
                        "createTime": "2022-03-17 16:23:12",
                        "updateTime": "2022-05-12 15:14:37",
                        "projectName": "南中高速",
                        "regionName": "TJ06",
                        "regionPathName": "南中高速/AI 超脑/TJ06"
                    }
                ]
            }
        }
        """
        provider_name = BenzhiProvider.objects.first().provider_name
        project_name = ProjectInfo.objects.first().project_name
        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        data = serializer.data
        data = list(map(lambda x: {
            'cameraId': x['cid'],
            'name': x['name'],
            'installLocation': x['site'],
            'longitude': '',
            'latitude': '',
            'createTime': x['create_time'],
            'updateTime': x['update_time'],
            'projectName': project_name,
            'regionName': '',
            'regionPathName': ''
        }, data))
        return Response({'ProviderName': provider_name, 'list': data})


class BenzhiMetadataViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = BenzhiMetadata


router = routers.DefaultRouter()
router.register('benzhiproviders', BenzhiProviderViewSet)
router.register('benzhisubcriptions', BenzhiSubscriptionViewSet)
router.register('benzhimetadatas', BenzhiMetadataViewSet)
