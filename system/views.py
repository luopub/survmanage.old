from django.shortcuts import render
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase

from .models import ProjectInfo


class ProjectInfoViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ProjectInfo


router = routers.DefaultRouter()
router.register('projectinfos', ProjectInfoViewSet)
