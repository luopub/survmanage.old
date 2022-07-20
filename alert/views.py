from django.shortcuts import render
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase

from .models import Alert


class AlertViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Alert


router = routers.DefaultRouter()
router.register('alerts', AlertViewSet)
