# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-24 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20171010_2157'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genero',
            new_name='Categoria',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='genero',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='genero',
            new_name='categoria',
        ),
    ]
