from rest_framework import generics, viewsets, renderers
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from .filters import ItemFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_class = ItemFilter
    permission_classes = (IsAuthenticated,)