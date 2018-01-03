from rest_framework.serializers import  *
from apps.users.models import *
from apps.notifications.models import * 
 

from rest_framework.authtoken.models import Token

#########################################
##  SERIALIZERS MODULE USERS           ## 
#########################################
class UserSerializer(ModelSerializer):
	class Meta:		 
		model = User 
		fields = ('pk','first_name','username','email','join_date','is_active','is_staff','password',)

	def create(self, validated_data):
	    user = User(
	        email=validated_data['email'],
	        username=validated_data['username']
	    )
	    user.set_password(validated_data['password'])
	    user.save()
	    return user

 
#########################################
##  SERIALIZERS MODULE NOTIFICATIONS   ## 
#########################################

class MessageSerializer(ModelSerializer):
	class Meta:
		model = Message
		fields = ('pk','from_user','to_user','desc','date_time','status')




 

















