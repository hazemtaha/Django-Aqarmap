from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from properties.models import PROPERTIES_TYPES
# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=20)  # need to be updated later
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    location_desc = models.TextField()
    services = models.TextField()
    owner = models.ForeignKey(User)


class ProjectProperties(models.Model):
    project = models.ForeignKey(Projects)
    property_type = models.CharField(max_length=1, choices=PROPERTIES_TYPES)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    min_size = models.FloatField()
    max_size = models.FloatField()


class ProjectsPayments(models.Model):
    project = models.ForeignKey(Projects)
    payment_method = models.CharField(max_length=50)  # need updating


class ProjectPhotos(models.Model):
    project = models.ForeignKey(Projects)
    photo = models.ImageField()
