from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import *

from apps.drp.views import new_token

def resetPasswordView(request):
    if request.POST:        
        email_user = request.POST['email_user']
        user_selected = User.objects.filter(email=email_user)
        if user_selected.count() > 0:
            new_token(user_selected[0].id) 
        else:
            pass

        return redirect('indexDashboard')

    else:
        data = {}
        return render(request, 'resetPassword.html',data)


 
