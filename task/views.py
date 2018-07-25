from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, renderers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.response import Response
from cauth.models import User
from .models import TaskResult, Task, CaseFile, Case
from .serializers import TaskSerializer, TaskEasySerializer, TaskResultSerializer, CaseSerializer, CaseFileSerializer
from .filters import TaskFilter, TaskResultFilter, CaseFilter, CaseFileFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['post'])
    def verify(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if not task.can_verify():
            return Response('只有草稿状态的任务可以进行审核')
        verifier_id = request.data.get('verifier_id')
        if verifier_id:
            verifier = User.objects.filter(pk=verifier_id).first()
        else:
            verifier = request.user
        res = task.verify(verifier)
        if res == 'success':
            return Response('审核成功')
        else:
            return Response(res)

    @action(detail=True, methods=['post'])
    def allocate(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.allocate()
        return Response('已设定任务为分配')

    @action(detail=True, methods=['post'])
    def finish(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.finish()
        return Response('已设定任务为完成')

class TaskResultViewSet(viewsets.ModelViewSet):
    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer
    filter_class = TaskResultFilter
    permission_classes = (IsAuthenticated,)


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    filter_class = CaseFilter
    permission_classes = (IsAuthenticated,)


class CaseFileViewSet(viewsets.ModelViewSet):
    queryset = CaseFile.objects.all()
    serializer_class = CaseFileSerializer
    filter_class = CaseFileFilter
    permission_classes = (IsAuthenticated,)