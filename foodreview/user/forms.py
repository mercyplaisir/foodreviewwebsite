from typing import Any,Protocol
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser
from .models import Restaurant_owner

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

class RestaurantOwnerSignupForm(UserCreationForm):
    class Meta:
        model = Restaurant_owner
        fields = ['first_name','last_name','email','password1','password2']
