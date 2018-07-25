from rest_framework import serializers
from cauth.serializers import UserEasySerializer
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    created_by = UserEasySerializer(many=False, read_only=True)
    # created_by_id = serializers.IntegerField()
    class Meta:
        model = Device
        fields = ('id', 'serial_number', 'device_model', 'kind', 'version', 'manufacturer',
                  'system', 'owner', 'created_by', 'created_by_id', 'create_time', 'last_modified', 'status',
                  'resolution', 'comment')


class DeviceEasySerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name')