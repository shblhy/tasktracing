from django.conf.urls import url, include
from rest_framework import routers
from device.views import DeviceViewSet
router = routers.DefaultRouter(trailing_slash=False)
router.register('', DeviceViewSet)


urlpatterns = [
    url('', include(router.urls)),
]
