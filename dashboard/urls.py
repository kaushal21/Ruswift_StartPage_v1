from django.conf.urls import include, url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'dashboard/$', views.index, name='index'),
]
