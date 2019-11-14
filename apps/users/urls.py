from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^resetpassword$', views.resetPasswordView, name='resetPasswordView'),
]


