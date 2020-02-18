from factory import SubFactory
from factory.django import DjangoModelFactory, ImageField
from factory.fuzzy import FuzzyText

from photo.photos.models import Photo
from photo.users.tests.factories import UserFactory


class PhotoFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    caption = FuzzyText()
    image = ImageField()

    class Meta:
        model = Photo
