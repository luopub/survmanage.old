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


router = routers.DefaultRouter()
router.register('algorithms', AlgorithmViewSet)
router.register('algorithmdefaultparameters', AlgorithmParametersDefaultViewSet)
