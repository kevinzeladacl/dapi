from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexDashboard,name="indexDashboard"),
 


    
 	#MODULE USERS
    url(r'^users/list$', views.listUserDashboard,name="listUserDashboard"),
    url(r'^users/create$', views.createUserDashboard,name="createUserDashboard"),
    url(r'^users/view/(?P<pk>[0-9]+)/$', views.viewUserDashboard,name="viewUserDashboard"),
    url(r'^users/update/(?P<pk>[0-9]+)/$', views.updateUserDashboard,name="updateUserDashboard"),
    url(r'^users/delete/(?P<pk>[0-9]+)/$', views.deleteUserDashboard,name="deleteUserDashboard"),

	 

]

