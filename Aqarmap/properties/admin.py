from django.contrib import admin

# Register your models here. to add sth into admin we will import our model into admin
from .models import Properties,PropertiesPhotos

admin.site.register(Properties)
admin.site.register(PropertiesPhotos)
