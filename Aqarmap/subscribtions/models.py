from __future__ import unicode_literals

from django.db import models
from accounts.models import UserProfile
from django.contrib.auth.models import User
from cities_light.models import City, Region
from properties.models import PROPERTIES_TYPES, PROPERTIES_CATEGORIES
# Create your models here.


class Subscribtions(models.Model):
    user = models.ForeignKey(UserProfile)
    city = models.ForeignKey(Region)  # need updating
    neighborhood = models.ForeignKey(City)  # need updating
    property_type = models.CharField(max_length=50, choices=PROPERTIES_TYPES)
    property_categories = models.CharField(
        max_length=1, choices=PROPERTIES_CATEGORIES)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    status = models.BooleanField(default=True)
