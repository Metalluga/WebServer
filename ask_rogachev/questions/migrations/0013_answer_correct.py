# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_auto_20161218_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]