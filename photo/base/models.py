from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class LogBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_created_by',
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_updated_by',
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
