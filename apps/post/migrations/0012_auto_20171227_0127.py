# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-27 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20171227_0417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagen2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='imagen3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='imagen4',
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.URLField(null=True),
        ),
    ]
