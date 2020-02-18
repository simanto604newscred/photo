from typing import Sequence, Any

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory


User = get_user_model()


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')
    email = Faker('email')
    is_staff = True
    is_active = True
    is_superuser = True

    class Meta:
        model = User
        django_get_or_create = ['email']

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = Faker(
            'password',
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(extra_kwargs={})
        self.set_password(password)
