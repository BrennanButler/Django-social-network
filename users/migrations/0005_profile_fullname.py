# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170219_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fullname',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
