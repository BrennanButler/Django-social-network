from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Emotion(models.Model):
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return "[" + str(self.id) + "] Emotion"


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    emotion = models.OneToOneField(Emotion, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[" + str(self.id) + "][" + str(self.datetime) + "]" + "Post by " + self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    emotion = models.OneToOneField(Emotion, on_delete=models.CASCADE)

    def __str__(self):
        return "[" + str(self.id) + "] comment by " + self.user.username
