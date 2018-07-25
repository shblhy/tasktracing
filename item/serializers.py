from rest_framework import serializers
from cauth.serializers import UserEasySerializer
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    created_by = UserEasySerializer(many=False)
    users = UserEasySerializer(many=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'desc', 'status', 'created_by', 'create_time', 'last_modified', 'weight',
                  'users', 'comment')


class ItemEasySerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name')