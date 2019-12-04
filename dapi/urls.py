from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from dapi.settings import local
from django.conf.urls.static import static
from dapi.settings import base
from django.conf.urls.static import static

urlpatterns = [
    
	#custom dapi
	path('api/v1/', include('apps.api.urls')),
	path('dashboard/', include('apps.dashboard.urls')),
	path('users/', include('apps.users.urls')),
	path('reset_password/', include('apps.drp.urls')),
	#default
    path('admin/', admin.site.urls),

]+ static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)