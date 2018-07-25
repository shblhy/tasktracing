from exlib.django_filters.filterset import NatualFilterSet
from .models import Item


class ItemFilter(NatualFilterSet):
    class Meta:
        model = Item
        fields = {
            'id': ['exact'],
            'name': ['icontains'],
            'status': ['exact'],
            'created_by': ['exact'],
            'comment': ['icontains'],
            'weight': ['exact'],
            'users': ['exact']
        }