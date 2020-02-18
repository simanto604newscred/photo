from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

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

    @action(detail=False, permission_classes=[IsAuthenticated])
    def my_photos(self, request, *args, **kwargs):

        try:
            # remember old state
            data = self.request.query_params
            _mutable = data._mutable

            # set to mutable
            data._mutable = True

            # update the user query parameter to logged in user id
            data['user'] = self.request.user.id

            # set mutable flag back
            data._mutable = _mutable
        except KeyError:
            pass

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
