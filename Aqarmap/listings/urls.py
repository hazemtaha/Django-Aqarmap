from django.conf.urls import url
from . import views

app_name = 'listing'

urlpatterns = [

    url(r'^listProperties/$', views.listProperties, name='listProperties'),
    url(r'^editProperties/(?P<prop_id>[0-9]+)/$', views.EditProp, name='editproperty')

]
