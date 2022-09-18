import platform
import os
from ruamel.yaml import YAML
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings
from rest_framework.authtoken.models import Token

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.error_code import ErrorCode
from utils.code_message_exception import CodeMsgException

from channel.models import Channel, ChannelAlgorithm
from algorithm.models import Algorithm, AlgorithmDefaultParameters
from alert.models import Alert

from .models import *


class BenzhiProviderViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = BenzhiProvider


class BenzhiSubscriptionViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = BenzhiSubscription


class BenzhiMetadataViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = BenzhiMetadata


router = routers.DefaultRouter()
router.register('benzhiproviders', BenzhiProviderViewSet)
router.register('benzhisubcriptions', BenzhiSubscriptionViewSet)
router.register('benzhimetadatas', BenzhiMetadataViewSet)
