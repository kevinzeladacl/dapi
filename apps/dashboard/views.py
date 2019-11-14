from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from .forms import *
from django.template.defaulttags import register


@register.filter()
def get_item(dictionary, key):
    return dictionary.get(key)






@login_required(login_url='loginDashboard')
def indexDashboard(request):


 
    count_users  = User.objects.filter().exclude(is_staff=True).count()
    data = {
        "count_users":count_users,
    }
    return render(request,'indexDashboard.html',data)


def loginDashboard(request):
    if request.user.is_authenticated:
        return redirect('indexDashboard')
    else:
        if 'login_form' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
                if user is not None:
                    try:
                        if user.is_active:
                            login(request, user)
                            return redirect('indexDashboard')
                    except:
                        login_form = LoginForm()
                        dataErrorLogin = "Lo sentimos, su usuario no esta habilitado para ingresar al sistema"
                        return render(request, 'loginUser.html', {'login_form': login_form, 'dataErrorLogin': dataErrorLogin})
                else:
                    login_form = LoginForm()
                    dataErrorLogin = "Usuario y/o contraseña no son válidos"
                    return render(request, 'loginUser.html', {'login_form': login_form, 'dataErrorLogin': dataErrorLogin})
            else:
                raise ('Error Login : Form Invalid')
        else:
            login_form = LoginForm()
            return render(request, 'loginUser.html', {'login_form': login_form})

def logoutDashboard(request):
    logout(request)
    return redirect('/')


 

#####################################
##  VIEWS MODULE USUARIO         ## 
#####################################


@login_required(login_url='loginView')
def listUserDashboard(request):
   
    list_users = User.objects.filter().exclude(is_staff=True)
    data = {
              
             "list_users":list_users,
        }
    return render(request,'listUserDashboard.html',data)


@login_required(login_url='loginView')
def createUserDashboard(request):
   
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
               
                "form":form,
            }
            return render(request,"createUserDashboard.html",data)
    else:
        form = createUserForm()
        data = {
            
            "form":form,
        }
        return render(request,"createUserDashboard.html",data)


@login_required(login_url='loginView')
def updateUserDashboard(request,pk):
    user_to_update = User.objects.get(pk=pk)
   
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
               
                "form":form,
            }
            return render(request,"updateUserDashboard.html",data)
    else:
        form = updateUserForm(instance=user_to_update)
        data = { 
            
            "form":form,
        }
        return render(request,"updateUserDashboard.html",data)


@login_required(login_url='loginView')
def deleteUserDashboard(request,pk):
   
    User.objects.get(pk=pk).delete()
    return redirect('listUserDashboard')
 

@login_required(login_url='loginView')
def viewUserDashboard(request,pk):
   
    user = User.objects.get(pk=pk)
    data = { 
       
        "user":user,
    }
    return render(request,'viewUserDashboard.html',data)   