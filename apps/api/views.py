#/general
from apps.api.serializers import *
from django.db.models import Q
from datetime import date, timedelta
from django.http import HttpResponse

#drf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser 
from django_filters.rest_framework import DjangoFilterBackend

#models
from apps.users.models import *




#####################################
##  VIEWS MODULE USERS            ## 
#####################################

class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserCreate(generics.CreateAPIView):
	permission_classes = (AllowAny,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

 
