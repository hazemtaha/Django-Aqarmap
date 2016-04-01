from django.conf.urls import url

from . import views
app_name = 'search'
urlpatterns = [
    url(r'^$', views.main_search, name="index"),
    url(r'^results/', views.search_results, name="results"),
    url(r'^compare/(?P<first_prop>[0-9]+)/(?P<second_prop>[0-9]+)/$',
        views.property_compare, name="compare"),
]
