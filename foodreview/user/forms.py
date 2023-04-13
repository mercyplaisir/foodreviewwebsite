from typing import Any
from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import random



class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']

# class UserProfileForm(forms.Form):
#     """a user profil form

#     Args:
#         forms (django.form): _description_
#     """
#     d_o_b = forms.DateTimeField()
#     phone_number = forms.CharField()
#     class Meta:
#         """"""
#         model= User
#         fields = ['d_o_b','phone_number'] 