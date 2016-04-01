from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# from properties.models import Properties
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
CURRENCY = (
    ('EGP', 'EGP'),
    ('USD', 'USD'),
)


def upload_location(instace, filename):
    ProfileModel = instace.__class__
    new_id = ProfileModel.objects.order_by('id').last().id + 1
    return "%s/%s" % (new_id, filename)


class UserProfile(AbstractUser):

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # update this field with choices field or auto generated countries
    country = models.CharField(max_length=50)
    default_currency = models.CharField(
        max_length=3, choices=CURRENCY)  # update this field like above
    phone_number = models.CharField(max_length=11)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPES)
    _image = models.ImageField(upload_to=upload_location,
                               null=True, blank=True, width_field="img_width", height_field="img_height")
    img_height = models.IntegerField(default=0)
    img_width = models.IntegerField(default=0)
    points = models.IntegerField(default=100)
    social_media = models.BooleanField(default=False)
    messages = models.ManyToManyField(
        'self', through='UserMessages', symmetrical=False)

    def __str__(self):
        return self.username


class UserMessages(models.Model):
    reciever = models.ForeignKey(UserProfile, related_name="reciever")
    sender = models.ForeignKey(UserProfile, related_name="sender")
    prop = models.ForeignKey('properties.Properties')
    msg_body = models.TextField()
