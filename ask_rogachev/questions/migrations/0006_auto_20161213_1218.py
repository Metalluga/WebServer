# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 12:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0005_auto_20161213_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='publications',
        ),
        migrations.RemoveField(
            model_name='question',
            name='like',
        ),
        migrations.AddField(
            model_name='like',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]