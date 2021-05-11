from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView


app_name = 'homepages'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about-us/$', views.aboutus, name='about-us'),
    url(r'services/$', views.services, name='services'),
    url(r'login/$', LoginView.as_view(template_name='homepages/login.html'), name='login'),
    url(r'sing-up/$', views.signup, name='sing-up'),
    url(r'help/$', views.help, name='help'),
    url(r'postlogin/$', views.postlogin, name='postlogin'),
    url(r'postsignup/$', views.postsignup, name='postsignup'),
]

