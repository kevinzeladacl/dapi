from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import *
 

def loginView(request):
    if request.user.is_authenticated():
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



def logoutView(request):
    logout(request)
    return redirect('loginView')


 