# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-17 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20170413_1811'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFavorite',
            new_name='UserFavourite',
        ),
    ]