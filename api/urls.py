from django.urls import path, re_path, include
from alert.views import router as alert_router
from algorithm.views import router as algorithm_router
from channel.views import router as channel_router
from push.views import router as push_router
from system.views import router as system_router
from rest_framework.authtoken.views import obtain_auth_token
from upload.views import router as upload_router
from interface.views import router as interface_router

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('alert/', include(alert_router.urls)),
    path('algorithm/', include(algorithm_router.urls)),
    path('channel/', include(channel_router.urls)),
    path('system/', include(system_router.urls)),
    path('upload/', include(upload_router.urls)),
    path('interface/', include(interface_router.urls)),
]
