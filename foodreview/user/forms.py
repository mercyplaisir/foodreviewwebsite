from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser
from .custom.group import Restaurant_owner_group

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

class RestaurantOwnerSignupForm(CustomerSignupForm):
    def save(self, commit: bool = ...) -> Any:
        user:CustomUser = super(RestaurantOwnerSignupForm,self).save()
        gr = Restaurant_owner_group.group()
        user.groups.add(gr)
        if commit:
            user.save()
        
        return user