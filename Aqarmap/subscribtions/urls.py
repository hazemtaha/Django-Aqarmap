from django.conf.urls import url
from . import views
app_name = 'subscribtions'
urlpatterns = [
	url(r'^$', views.subscribtions, name='subscribtions'),
	url(r'^add_subscribtion/', views.add_subscribtion, name='add_subscribtion'),
	url(r'^active/', views.active, name='active'),
	url(r'^delete_sub/', views.delete_sub, name='delete_sub'),
	url(r'^sub_results/', views.sub_results, name='sub_results'),
	]
