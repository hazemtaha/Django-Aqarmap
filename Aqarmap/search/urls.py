from django.conf.urls import url

from . import views
app_name = 'search'
urlpatterns = [
    url(r'^$', views.main_search, name="index"),
    url(r'^search/results/', views.search_results, name="index"),
]
