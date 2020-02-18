from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photo.photos.models import Photo
from photo.photos.serializers import PhotoSerializer


class PhotosViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    ordering_fields = ['created_at']
    filterset_fields = ('user', 'is_draft', 'caption')