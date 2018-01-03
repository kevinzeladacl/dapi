from django import forms
from apps.users.models import *
from apps.notifications.models import *
 
 
class createUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'true'
            }),
             'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'true'
            }),
             'username': forms.TextInput(attrs={
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
            'password': forms.TextInput(attrs={
                'type': 'password',
                'class': 'form-control',
                'required': 'true'
            }),
        }

class updateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'true'
            }),
             'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'true'
            }),
             'username': forms.TextInput(attrs={
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
            'password': forms.TextInput(attrs={
                'type': 'password',
                'class': 'form-control',
                'required': 'true'
            }),
        }
 


 
