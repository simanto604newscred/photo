from django.urls import reverse
from pytest import fixture

import json

from photo.photos.models import Photo
from photo.photos.tests.factories import PhotoFactory


class BasePhoto:

    @fixture(autouse=True)
    def make_data(self, user):
        PhotoFactory(user=user)
        PhotoFactory(user=user, is_draft=True)
        PhotoFactory()


class TestListAllPhotos(BasePhoto):

    url = reverse('api:photos-list')

    def test_list_all_photos(self, client):
        response = client.get(self.url)

        assert response.status_code == 200
        assert response.data.get('count', 0) == 3


class TestUserPhotos(BasePhoto):

    url = reverse('api:photos-list')
    caption = 'some caption'

    def test_list_user_photos(self, auth_client):
        response = auth_client.get(self.url)

        assert response.status_code == 200
        assert response.data.get('count', 0) == 3

    def test_create_user_photos(self, auth_client, user):
        data = {
            'user': user.id,
            'image': "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1"
                     "BMVEUAAACnej3aAAAAAXRSTlMAQObYZgAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=",

            'caption': self.caption,
            'is_draft': True
        }

        response = auth_client.post(self.url, data=data)

        assert response.status_code == 201
        assert Photo.objects.filter(
            user_id=user.id,
            caption__exact=self.caption,
            image__isnull=False
        ).exists()

    def test_create_bulk_user_photos(self, auth_client, user):
        data = [{
            'user': user.id,
            'image': "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1"
                     "BMVEUAAACnej3aAAAAAXRSTlMAQObYZgAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=",
            'caption': self.caption,
            'is_draft': False
        } for _ in range(4)]

        data = {'images': data}
        response = auth_client.post(self.url, data=json.dumps(data), content_type="application/json")

        assert response.status_code == 201
        assert Photo.objects.filter(
            user_id=user.id,
            caption__exact=self.caption,
            image__isnull=False
        ).count() == 4
