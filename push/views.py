from django.shortcuts import render
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase

from .models import Push, PushUrl


class PushViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Push


class PushUrlViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = PushUrl


router = routers.DefaultRouter()
router.register('pushes', PushViewSet)
router.register('pushurls', PushUrlViewSet)
