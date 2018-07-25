from rest_framework import generics, viewsets, renderers
from rest_framework.permissions import IsAuthenticated
from device.models import Device
from .serializers import DeviceSerializer
from .filters import DeviceFilter


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_class = DeviceFilter
    permission_classes = (IsAuthenticated,)