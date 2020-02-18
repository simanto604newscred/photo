from pytest import fixture
from rest_framework.test import APIClient

from photo.users.tests.factories import UserFactory


@fixture
def user():
    return UserFactory()


@fixture(autouse=True)
def enable_db_access(db):
    pass


@fixture
def client():
    return APIClient()


@fixture
def auth_client(user, client):
    client.force_authenticate(user)
    return client
