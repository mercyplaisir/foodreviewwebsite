import datetime
from typing import Any
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser


class CustomerSignupForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','password1','password2']

class CustomerChangeForm(UserChangeForm):
    # d_o_b = forms.DateField(
    #     widget= forms.SelectDateWidget(years=[str(i) for i in range(1982,2023)])
    # )
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','d_o_b']
    