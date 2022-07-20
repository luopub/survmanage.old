from django.shortcuts import render
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase

from .models import Channel, ChannelAlgorithm


class ChannelViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Channel


class ChannelAlgorithmViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ChannelAlgorithm


router = routers.DefaultRouter()
router.register('channels', ChannelViewSet)
router.register('channelalgorithms', ChannelAlgorithmViewSet)
