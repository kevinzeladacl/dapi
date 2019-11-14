from django.contrib import admin
from django.urls import path,include

from . import views
 
urlpatterns = [
    
     
	
    #User
    path('', views.indexDashboard ,name="indexDashboard"),    
    path('login/', views.loginDashboard ,name="loginDashboard"),
    path('logout/', views.logoutDashboard ,name="logoutDashboard"),
    # path('register/', views.registerDashboard ,name="registerDashboard"),
     

    #MODULE USERS
    path('users/list', views.listUserDashboard,name="listUserDashboard"),
    path('users/create', views.createUserDashboard,name="createUserDashboard"),
    path('users/view/<pk>', views.viewUserDashboard,name="viewUserDashboard"),
    path('users/update/<pk>', views.updateUserDashboard,name="updateUserDashboard"),
    path('users/delete/<pk>', views.deleteUserDashboard,name="deleteUserDashboard"),
 


]

