from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^login$', views.loginView, name='loginView'),
    url(r'^logout$', views.logoutView, name='logoutView'),
    
]


