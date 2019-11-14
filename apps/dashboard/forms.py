from django import forms
from apps.users.models import *
from apps.agreements.models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
       widget=forms.TextInput(attrs={
           'class': 'form-control',
           'placeholder':"Ingresa tu Correo",
           'required': 'true',
       }))
    password = forms.CharField(max_length=30,
       widget=forms.TextInput(attrs={
           'type': 'password',
           'class': 'form-control',
           'placeholder':"Ingresa tu Clave",
           'required': 'true'
       }))


class updateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email','type_user')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'true'
            }),
             'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'true'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': 'true'
            }),

             'type_user': forms.Select(attrs={
                'class': 'form-control',
                'required': 'true'
            }),
 
        }
