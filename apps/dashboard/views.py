from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from apps.users.models import *
from apps.dashboard.forms import *
from apps.notifications.models import *
 

#####################################
##  VIEWS GENERAL                  ## 
#####################################
@login_required(login_url='loginView')
def indexDashboard(request):
	data = {

	}

	return render(request,'indexDashboard.html',data)
 

	
#####################################
##  VIEWS MODULE USERS            ## 
#####################################

@login_required(login_url='loginView')
def listUserDashboard(request):
	mesagges = Message.objects.filter(to_user=request.user,status=0)
	mesagges_count = Message.objects.filter(to_user=request.user,status=0).count()
	list_users = User.objects.filter()
	data = {
			 "mesagges":mesagges,
			 "mesagges_count":mesagges_count,
			 "list_users":list_users,
		}
	return render(request,'listUserDashboard.html',data)


@login_required(login_url='loginView')
def createUserDashboard(request):
	mesagges = Message.objects.filter(to_user=request.user,status=0)
	mesagges_count = Message.objects.filter(to_user=request.user,status=0).count()
	if request.POST:
		form = createUserForm(request.POST,request.FILES)
		if form.is_valid():
			f = form.save(commit=False)
			f.save()
			user_new = User.objects.last()
			user_new.set_password(user_new.password)
			user_new.save()
			return redirect('listUserDashboard')
		else:
			form = createUserForm()
			data = {		 
				"mesagges":mesagges,
				"mesagges_count":mesagges_count,
				"form":form,
			}
			return render(request,"createUserDashboard.html",data)
	else:
		form = createUserForm()
		data = {
			"mesagges":mesagges,
			"mesagges_count":mesagges_count,
			"form":form,
		}
		return render(request,"createUserDashboard.html",data)


@login_required(login_url='loginView')
def updateUserDashboard(request,pk):
	user_to_update = User.objects.get(pk=pk)
	mesagges = Message.objects.filter(to_user=request.user,status=0)
	mesagges_count = Message.objects.filter(to_user=request.user,status=0).count()
	if request.POST:
		form = updateUserForm(request.POST,request.FILES,instance=user_to_update)
		if form.is_valid():
			f = form.save(commit=False)
			f.save()
			user_to_update.set_password(user_to_update.password)
			user_to_update.save()
			return redirect('listUserDashboard')
		else:
			form = updateUserForm(instance=user_to_update)
			data = {	 
				"mesagges":mesagges,
				"mesagges_count":mesagges_count,
				"form":form,
			}
			return render(request,"updateUserDashboard.html",data)
	else:
		form = updateUserForm(instance=user_to_update)
		data = { 
			"mesagges":mesagges,
			"mesagges_count":mesagges_count,
			"form":form,
		}
		return render(request,"updateUserDashboard.html",data)


@login_required(login_url='loginView')
def deleteUserDashboard(request,pk):
	mesagges = Message.objects.filter(to_user=request.user,status=0)
	mesagges_count = Message.objects.filter(to_user=request.user,status=0).count()
	User.objects.get(pk=pk).delete()
	return redirect('listUserDashboard')
 

@login_required(login_url='loginView')
def viewUserDashboard(request,pk):
	mesagges = Message.objects.filter(to_user=request.user,status=0)
	mesagges_count = Message.objects.filter(to_user=request.user,status=0).count()
	user = User.objects.get(pk=pk)
	data = { 
		"mesagges":mesagges,
		"mesagges_count":mesagges_count,
	    "user":user,
	}
	return render(request,'viewUserDashboard.html',data)

 
	 
