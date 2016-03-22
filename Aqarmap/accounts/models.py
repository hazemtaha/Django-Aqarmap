from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from properties.models import Properties
# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
ACCOUNT_TYPES = (
    ('BR', 'Buyer/Renter'),
    ('PO', 'Private Owner'),
    ('B', 'Broker'),
    ('RC', 'Real Estate Company'),
)


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # update this field with choices field or auto generated countries
    country = models.CharField(max_length=50)
    default_currency = models.CharField(
        max_length=50)  # update this field like above
    phone_number = models.CharField(max_length=11)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPES)
    image = models.ImageField()
    points = models.IntegerField()
    social_media = models.BooleanField(default=False)
    messages = models.ManyToManyField(
        'self', through='UserMessages', symmetrical=False)


class UserMessages(models.Model):
    reciever = models.ForeignKey(UserProfile, related_name="reciever")
    sender = models.ForeignKey(UserProfile, related_name="sender")
    prop = models.ForeignKey(Properties)
    msg_body = models.TextField()
