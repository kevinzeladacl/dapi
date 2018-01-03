from apps.api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser 
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from apps.users.models import *
from apps.notifications.models import *
 
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
import json
 


#####################################
##  VIEWS  USERS     MODULE       ## 
#####################################




class CurrentUserView(APIView):
	def get(self, request):
		user = request.user
		serializer = UserSerializer(user)
		#check level
		total_points_answer = AnswerUser.objects.filter(user=user).aggregate(Sum('answer__points'))
		points = total_points_answer["answer__points__sum"]
		if points is None or '':
			points = 0
		levels = LevelUser.objects.filter(points_requiered__lte=points)
		level_select = levels.last()
		user_update = User.objects.filter(id=user.id).update(level_user=level_select)
		return Response(serializer.data)

 


class UserList(generics.ListCreateAPIView):
	permission_classes = (AllowAny,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

 

#####################################
##  VIEWS MODULE NOTIFICATIONS     ## 
#####################################
class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(Q(to_user__user=self.request.user )| Q(from_user__user=self.request.user) ).distinct().order_by('-date_time')
 

    

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
        Message.objects.filter(pk=self.kwargs["pk"]).update(status=1)
        return Message.objects.filter(pk=self.kwargs["pk"])
 
 


 










