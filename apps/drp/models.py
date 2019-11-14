from django.db import models
from apps.users.models import User


class TokenResetPassword(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	status = models.BooleanField(default=True)
	token = models.CharField(max_length=25)
	date = models.DateTimeField(auto_now_add=True)

