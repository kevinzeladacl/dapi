from django.shortcuts import render,redirect
from django.core.mail import send_mail, EmailMessage
from django.utils.crypto import get_random_string
from dapi.settings import base

from .models import TokenResetPassword
from apps.users.models import User

from .forms import changepasswordForm



import datetime


def new_token(user_id):
	user = User.objects.get(pk=user_id)
	token_generate = get_random_string(length=25)
	TokenResetPassword.objects.create(user=user,token=token_generate)

	link = base.URL_DOMAIN + '/reset_password/token/' + token_generate     
	msg = "Hello to continue with the password change click on the following link where you will be asked for the new password. \n\nRemember that this link only lasts 5 minutes before expiring. \n\n %s "  % link

	user_email = user.email
	email = EmailMessage('Reset Password', msg , to=[user_email])
	email.send()


	return True

def check_token(request,token):

	token_check = TokenResetPassword.objects.get(token=token)

	time_check = datetime.datetime.now() - token_check.date 

	
	if time_check.seconds > 11300 or token_check.status == False:
		print("Paso mucho tiempo")


		data = {
		 
		}
		return render(request,'nochangepassword.html',data)

	else:
 
		if request.POST:
			form = changepasswordForm(request.POST)
			if form.is_valid():
				user_to_update = User.objects.get(pk=token_check.user.id)
				user_to_update.set_password(form.cleaned_data['password'] )
				user_to_update.save()
				TokenResetPassword.objects.filter(token=token).update(status=False)
				return redirect('indexDashboard')
		else:
			form = changepasswordForm()
			data = {
			"form":form,
			}
			return render(request,'changepassword.html',data)
