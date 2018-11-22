from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static

from dapi import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/'+ settings.API_VERSION +"/", include('apps.api.urls')),
    url(r'^',include('apps.dashboard.urls')),
    url(r'^users/',include('apps.users.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
