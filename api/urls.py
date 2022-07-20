from django.urls import path, re_path, include
from alert.views import router as alert_router
from algorithm.views import router as algorithm_router
from channel.views import router as channel_router
from push.views import router as push_router
from system.views import router as system_router

urlpatterns = [
    path('alert/', include(alert_router.urls)),
    path('algorithm/', include(algorithm_router.urls)),
    path('channel/', include(channel_router.urls)),
    path('system/', include(system_router.urls)),
]
