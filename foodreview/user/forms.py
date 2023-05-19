from typing import Any,Protocol
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser
from main.utils import get_group
from restaurant.groups import Restaurant_owner

class Group(Protocol):
    ...

class CustomerSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','password1','password2','is_restaurant_owner']

class CustomerChangeForm(UserChangeForm):
    # d_o_b = forms.DateField(
    #     widget= forms.SelectDateWidget(years=[str(i) for i in range(1982,2023)])
    # )
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','d_o_b','is_restaurant_owner']

class RestaurantOwnerSignupForm(CustomerSignupForm):
    
    def save(self,group, commit: bool = ...) -> Any:
        
        m = super(RestaurantOwnerSignupForm, self).save(commit=True)
        if commit:
            if self.cleaned_data['is_restaurant_owner']:
                m.groups.add(Group)
                m.save()
        return super(RestaurantOwnerSignupForm, self).save(commit)