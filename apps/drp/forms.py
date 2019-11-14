from django import forms
from .models import *

 


class changepasswordForm(forms.Form):

    password = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'required': 'true'
                               }))
     
