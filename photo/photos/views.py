from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photo.photos.models import Photo
from photo.photos.serializers import PhotoSerializer, PhotosSerializer


class PhotosFilter(FilterSet):
    is_draft = filters.BooleanFilter('is_draft')
    caption = filters.CharFilter('caption')

    class Meta:
        model = Photo
        fields = ('user', 'is_draft', 'caption')


class PhotosViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    ordering_fields = ['created_at']
    filterset_class = PhotosFilter

    def get_serializer(self, *args, **kwargs):
        kwargs.update(context={'request': self.request})
        if "data" in kwargs:
            data = kwargs["data"]
            images = data.get('images', None)

            if isinstance(images, list):
                return PhotosSerializer(*args, **kwargs)
        return PhotoSerializer(*args, **kwargs)
