from pytest import fixture


from photo.users.tests.factories import UserFactory


@fixture
def user():
    return UserFactory()


@fixture(autouse=True)
def enable_db_access(db):
    pass
