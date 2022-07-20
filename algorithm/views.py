from django.shortcuts import render
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase

from .models import Algorithm, AlgorithmParameters


class AlgorithmViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = Algorithm


class AlgorithmParametersViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = AlgorithmParameters


router = routers.DefaultRouter()
router.register('algorithms', AlgorithmViewSet)
router.register('algorithmparameters', AlgorithmParametersViewSet)
