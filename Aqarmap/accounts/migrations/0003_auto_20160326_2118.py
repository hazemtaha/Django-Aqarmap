# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160326_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='image',
            new_name='_image',
        ),
    ]
