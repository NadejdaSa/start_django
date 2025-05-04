from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrAdmin

class AdvertisementViewSet(ModelViewSet):

    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        return [AllowAny()]
