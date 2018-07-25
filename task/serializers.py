from rest_framework import serializers
from cauth.serializers import UserEasySerializer
from item.serializers import ItemEasySerializer
from .models import TaskResult, Task, CaseFile, Case


class TaskSerializer(serializers.ModelSerializer):
    created_by = UserEasySerializer(many=False)
    item = ItemEasySerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'item', 'test_case', 'start_time', 'end_time', 'commit', 'verify_ready_time', 'verifier',
                  'verify_time', 'allocate_time', 'executor_ids', 'executors', 'created_by', 'create_time',
                  'last_modified', 'status')


class TaskEasySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name')


class TaskResultSerializer(serializers.ModelSerializer):
    task = TaskEasySerializer(many=False)
    created_by = UserEasySerializer(many=False)

    class Meta:
        model = TaskResult
        fields = ('id', 'task', 'stage', 'status', 'desc',
                  'created_by', 'create_time')


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('id', 'item', 'function_name', 'state', 'precondition', 'desc', 'steps', 'expected_res',
                  'priority', 'new_added', 'comment', 'status', 'created_by', 'create_time', 'last_modified')


class CaseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseFile
        fields = ('id', 'case', 'name', 'filepath', 'created_by', 'create_time')