from django.contrib import admin

# Register your models here.

from .models import Profile, Notification, Relationship

admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(Relationship)
