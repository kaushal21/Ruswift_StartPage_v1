from django.contrib import admin
from django.conf.urls import include, url
from homepages import views

app_name = 'ruswift'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about-us/$', views.aboutus, name='about-us'),
    url(r'^services/$', views.services, name='services'),
    url(r'^login/$', views.login, name='login'),
    url(r'^postsignup/$', views.postsignup, name='postsignup'),
    url(r'^postlogin/$', views.postlogin, name='postlogin'),
    url(r'^sing-up/$', views.signup, name='sing-up'),
    url(r'^help/$', views.help, name='help'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'admin/', admin.site.urls),
]
