from django.urls import include, path
from . import views

urlpatterns = [
    path('token/<token>', views.check_token,name="check_token"),
 ]
