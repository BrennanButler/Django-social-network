from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from Image.models import Image, UserImage

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profilePic = models.ForeignKey(UserImage, on_delete=models.CASCADE)
    bio = models.CharField(max_length=120)
    employment = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return "[" + str(self.id) + "] " + self.user.username + " Profile"


# Note : Run a cron job at X interval to check and remove old notifications


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="NotificationUser")
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="NotificationImage")
    description = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)

    type = models.IntegerField(default=0)
    # type 0 = Site notification
    # type 1 = Friend notification
    # type 2 = Friend request notification

    def __str__(self):
        return "[" + str(self.id) + "] " + self.user.username + " Notification [" + str(self.datetime) + "]"


# NOTE: This may need a more elegant implementation. Currently there will be two records per relationship
class Relationship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="RelUser")
    corrUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 related_name="RelCorrespondingUser")

    status = models.IntegerField(default=0)
    # status 0 = Friend request sent but not accepted
    # status 1 = Friends
    # status 2 = Best friends
    # status 3 = Blocked

    def __str__(self):
        return "Relationship between " + self.user.username + " and " + self.corrUser.username + " status: " + \
               str(self.status)
