# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20161218_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Answer')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Profile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='answerlike',
            unique_together=set([('profile', 'answer')]),
        ),
    ]
