from exlib.django_filters.filterset import NatualFilterSet, CommonModelMultipleChoiceFilter
from .models import TaskResult, Task, CaseFile, Case


class TaskFilter(NatualFilterSet):
    # executors = CommonModelMultipleChoiceFilter(rel_field_name='executor_ids')

    class Meta:
        model = Task
        fields = {
            'id': ['exact'],
            'item': ['exact'],
            'status': ['exact'],
            'created_by': ['exact'],
            'verifier': ['exact'],
            'commit': ['icontains'],
        }


class TaskResultFilter(NatualFilterSet):
    class Meta:
        model = TaskResult
        fields = {
            'id': ['exact'],
            'task': ['exact'],
            'status': ['exact'],
            'created_by': ['exact'],
            'desc': ['icontains'],
            'stage': ['exact'],
        }


class CaseFilter(NatualFilterSet):
    class Meta:
        model = Case
        fields = {
            'id': ['exact'],
            'item': ['exact'],
            'status': ['exact'],
            'priority': ['exact'],
            'new_added': ['exact'],
            'comment': ['icontains'],
            'precondition': ['icontains'],
            'desc': ['icontains'],
            'state': ['exact'],
            'function_name': ['icontains'],
            'created_by': ['exact'],
        }


class CaseFileFilter(NatualFilterSet):
    class Meta:
        model = CaseFile
        fields = {
            'id': ['exact'],
            'name': ['icontains'],
            'case': ['exact'],
            'created_by': ['exact'],
        }