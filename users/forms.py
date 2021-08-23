from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=64)
    middle_name= forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email= forms.EmailField(required='False')

    class Meta:
        model= User
        fields= ['username','first_name','last_name','email','password1','password2']
