from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.subscribtions, name='subscribtions'),
	url(r'^$', views.subForm, name='subForm'),
	]
