from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
#This abstract base class just provides self-updating created and modified fields on any model that inherits from it.
# Create your models here.

PROPERTIES_TYPES = (
    ('a', 'Appartment'),
    ('b', 'Building'),
    ('l', 'Land'),
    ('v', 'Villa'),
    ('s', 'Store'),
    ('o', 'Office'),
)
PROPERTIES_CATEGORIES = (
    ('s', 'For Sale'),
    ('r', 'For Rent'),
)


class Properties(TimeStampedModel):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    prop_type = models.CharField(max_length=1, choices=PROPERTIES_TYPES)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=PROPERTIES_CATEGORIES)
    description = models.TextField()
    price = models.IntegerField()
    size = models.IntegerField()
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    yt_url = models.URLField()
    owner = models.ForeignKey(User)


class PropertiesPhotos(models.Model):
    prop_photo = models.ImageField()
    prop = models.ForeignKey(Properties, on_delete=models.CASCADE)
