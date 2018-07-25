from django.conf.urls import url, include
from rest_framework import routers
from item.views import ItemViewSet
router = routers.DefaultRouter(trailing_slash=False)
router.register('', ItemViewSet)


urlpatterns = [
    url('', include(router.urls)),
]
