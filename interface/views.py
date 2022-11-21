from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.datetime_utils import datetime_utc_to_local

from channel.models import Channel
from system.models import ProjectInfo

from .models import *


class BenzhiReportUrlViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = BenzhiReportUrl


class BenzhiSubscriptionViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = BenzhiSubscription

    authentication_classes = []
    permission_classes = []

    @action(detail=False, methods=['post'])
    def subscribe_all(self, request):
        self.model.on_activated()
        return Response({})

    @action(detail=False, methods=['get', 'post'])
    def get_subscription_types(self, request):
        """
        本质平台接口：
            3.1 事件类型订阅接
        调用：
            (post) https://cn-nn-dx-1.natfrp.cloud:21435/api/v1/interface/benzhisubcriptions/get_subscription_types/
        样本数据：
            {
                "code": 0,
                "msg": "Success",
                "message": "Success",
                "data": {
                    "ProviderName": "美云数字",
                    "list": [
                        {
                            "EventType": "person",
                            "EventTypeName": "区域入侵",
                            "IsSubscribed": true
                        },
                        {
                            "EventType": "no helmet",
                            "EventTypeName": "未戴安全帽",
                            "IsSubscribed": true
                        },
                        {
                            "EventType": "no clothing",
                            "EventTypeName": "未穿反光衣",
                            "IsSubscribed": true
                        },
                        {
                            "EventType": "no mask",
                            "EventTypeName": "未戴口罩",
                            "IsSubscribed": true
                        },
                        {
                            "EventType": "smoking",
                            "EventTypeName": "吸烟",
                            "IsSubscribed": true
                        },
                        {
                            "EventType": "slippers",
                            "EventTypeName": "拖鞋",
                            "IsSubscribed": true
                        },
                        {
                            "EventType": "call",
                            "EventTypeName": "打电话",
                            "IsSubscribed": true
                        },
                        {
                            "EventType": "play phone",
                            "EventTypeName": "玩手机",
                            "IsSubscribed": true
                        }
                    ]
                }
            }
        """
        provider_name = BenzhiReportUrl.objects.first().provider_name
        subscptions = self.model.objects.all().values('algorithm__name', 'algorithm__event_type', 'algorithm__name_ch', 'is_subscribed')
        subscptions = list(map(lambda x: {
            'EventType': x['algorithm__name'],  # x['algorithm__event_type'],
            'EventTypeName': x['algorithm__name_ch'],
            'IsSubscribed': x['is_subscribed']
        }, subscptions))
        return Response({'ProviderName': provider_name, 'list': subscptions})

    @action(detail=False, methods=['post'])
    def get_subscription_cameras(self, request):
        """
        本质平台接口：
            3.2 报警摄像头基础数据获得接⼝
        调用：
            (post) https://cn-nn-dx-1.natfrp.cloud:21435/api/v1/interface/benzhisubcriptions/get_subscription_cameras/
        样本数据：
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
        provider_name = BenzhiReportUrl.objects.first().provider_name
        project_name = ProjectInfo.objects.first().project_name
        channels = Channel.objects.all()
        data = [{
            'cameraId': x.cid,
            'name': x.name,
            'installLocation': x.site,
            'longitude': '',
            'latitude': '',
            'createTime': datetime_utc_to_local(x.create_time).strftime('%Y-%m-%d %H:%M:%S'),
            'updateTime': datetime_utc_to_local(x.update_time).strftime('%Y-%m-%d %H:%M:%S'),
            'projectName': project_name,
            'regionName': x.site,
            'regionPathName': ''
        } for x in channels]
        return Response({'ProviderName': provider_name, 'list': data})


router = routers.DefaultRouter()
router.register('benzhisubcriptions', BenzhiSubscriptionViewSet)
router.register('benzhireporturls', BenzhiReportUrlViewSet)
