# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 18:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fullname',
        ),
    ]
