from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
#This abstract base class just provides self-updating created and modified fields on any model that inherits from it.and you have to install it's package too from pip
from geoposition.fields import GeopositionField
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
    yt_url = models.URLField()
    position = GeopositionField()
    #owner = models.ForeignKey(User)
    #p = Properties(title="Alrehab",status="true",prop_type='l',city="sharkia",neighborhood="belbies",category='s',description="new and unique yeah",price="1000000",size="200",lat="140000.4545",lon="200000.2200",yt_url="https://www.youtube.com/watch?v=FoAqHxm5dpo")
    #save() for testing only
    def __str__(self):
        return self.title


class PropertiesPhotos(models.Model):
    prop_photo = models.ImageField()
    prop = models.ForeignKey(Properties, on_delete=models.CASCADE)
    #pp=p.propertiesphotos_set.create(prop_photo="image_path")
    #another test to link the foreign keys with each other
    def __str__(self):
        return str(self.prop_photo)
        #this for admin readability