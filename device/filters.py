from exlib.django_filters.filterset import NatualFilterSet
from .models import Device


class DeviceFilter(NatualFilterSet):
    class Meta:
        model = Device
        fields = {
            'id': ['exact'],
            'serial_number': ['exact'],
            'device_model': ['icontains'],
            'kind': ['exact'],
            'manufacturer': ['icontains'],
            'owner': ['exact'],
            'created_by': ['exact'],
            'status': ['exact'],
            'resolution': ['icontains']
        }