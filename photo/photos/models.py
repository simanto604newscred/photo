from django.contrib.auth import get_user_model
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

from photo.base.models import LogBase
from photo.photos.utils import image_path


User = get_user_model()
THUMBNAILER_OPTIONS = dict(size=(500, 500), sharpen=True)

class Photo(LogBase):
    user = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    is_draft = models.BooleanField(default=False)
    image = ThumbnailerImageField(upload_to=image_path,
                                  resize_source=THUMBNAILER_OPTIONS)

    def __str__(self):
        return "[ ID %s | Photo: %s ] " % (self.id, self.caption)
