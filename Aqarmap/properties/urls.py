from django.conf.urls import url
from . import views

app_name = 'properties'

urlpatterns = [
	url(r'^addproperty/$', views.addProperty, name='addproperty'),
	url(r'^propertiesforsale/properties_details/$', views.prop_details, name='properties_details'),
	url(r'^propertiesforsale/$', views.prop_forSale, name='propertiesforsale'),
	#ex addProperty/5 - send <prop_id> as an arguments | [0-9]+ sequences of digits
	#url(r'^(?P<prop_id>[0-9]+)/$', views.details, name='prop_details'),
	#url(r'^(?P<addProperty_id>[0-9])/$', views.addProperty, name='add'),
]