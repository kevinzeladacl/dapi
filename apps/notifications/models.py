from django.db import models
from apps.users.models import User
 

 
class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user')
    to_user = models.ForeignKey(User, related_name='to_user')
    desc = models.CharField(max_length=500)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)


 