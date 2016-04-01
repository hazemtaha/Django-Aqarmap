from django.conf.urls import url

from . import views
app_name = 'accounts'
urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.user_login, name="login"),

]
