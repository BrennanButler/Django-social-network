# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
