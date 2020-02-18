from drf_extra_fields.fields import Base64ImageField
from rest_framework.fields import BooleanField, CharField
from rest_framework.serializers import ModelSerializer

from photo.photos.models import Photo


class PhotoSerializer(ModelSerializer):
    image = Base64ImageField(required=True)
    is_draft = BooleanField(write_only=True)
    caption = CharField(max_length=300, required=True)

    class Meta:
        model = Photo
        fields = ['id', 'user', 'created_at', 'image', 'caption','is_draft' ]

