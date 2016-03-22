from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from properties.models import PROPERTIES_TYPES, PROPERTIES_CATEGORIES
# Create your models here.


class Subscribtions(models.Model):
    user = models.ForeignKey(User)
    city = models.CharField(max_length=50)  # need updating
    neighborhood = models.CharField(max_length=50)  # need updating
    property_type = models.CharField(max_length=1, choices=PROPERTIES_TYPES)
    property_categories = models.CharField(
        max_length=1, choices=PROPERTIES_CATEGORIES)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    status = models.BooleanField(default=True)
