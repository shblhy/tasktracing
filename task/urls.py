from django.conf.urls import url, include
from rest_framework import routers
from task.views import TaskViewSet, TaskResultViewSet, CaseViewSet, CaseFileViewSet
router = routers.DefaultRouter(trailing_slash=False)
router.register('tresult', TaskResultViewSet)
router.register('task', TaskViewSet)
router.register('cfile', CaseFileViewSet)
router.register('case', CaseViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
