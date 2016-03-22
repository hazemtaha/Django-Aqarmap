# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 22:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prop_Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_photo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('prop_type', models.CharField(choices=[('a', 'Appartment'), ('b', 'Building'), ('l', 'Land'), ('v', 'Villa'), ('s', 'Store'), ('o', 'Office')], max_length=1)),
                ('city', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('s', 'For Sale'), ('r', 'For Rent')], max_length=1)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('size', models.IntegerField()),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('yt_url', models.URLField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='prop_photos',
            name='prop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.Properties'),
        ),
    ]
