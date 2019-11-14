from django.contrib import admin
from django.urls import path,include

from django.conf.urls import url


from rest_framework.authtoken.views import obtain_auth_token



from rest_framework import permissions
 

from . import views


 

urlpatterns = [
    
    #custom
    path('auth/', obtain_auth_token), #login
    path('register/', views.UserCreate.as_view()),
    path('profile/', views.CurrentUserView.as_view()),

    #models
    path('users/', views.UserList.as_view()),  
    path('users/<pk>', views.UserDetail.as_view()),
   
    
 
]

