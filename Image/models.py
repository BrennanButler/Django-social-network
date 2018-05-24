from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Image(models.Model):
    file = models.FileField()


class UserImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    caption = models.TextField(null=True, blank=True)
