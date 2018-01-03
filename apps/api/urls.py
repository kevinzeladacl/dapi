from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from apps.api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
    #AUTHENTICATION
    url(r'^auth/', obtain_auth_token),
    #USERS MODULE
    url(r'^users/me$', views.CurrentUserView.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    #NOTIFICATION MODULE
    url(r'^message/$', views.MessageList.as_view(),name='MessageList'),
    url(r'^message/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view(),name='MessageDetail'),

 
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
