
from django.shortcuts import render
from .forms import (CustomerSignupForm,
                    CustomerChangeForm,
                    RestaurantOwnerSignupForm,
                    )
from django.contrib.auth import get_user_model,get_user
from .custom.group import Restaurant_owner_group
# Create your views here.


def login_page(response):
    return render(response,"user/login.html")

def signup_page(response):
    if response.method == "POST":
        form = CustomerSignupForm(response.POST)
        if form.is_valid():
            form.save(commit=True)            
    else:
        form= CustomerSignupForm()

    return render(response,"user/signup.html",{'form':form})

def user_update(response):
    user = response.user
    form = CustomerChangeForm(instance=user)
    return render(response,'user/user_update.html',{'form':form})

def restaurant_owner_signup_page(response):
    if response.method == "POST":
        form = RestaurantOwnerSignupForm(response.POST)
        if form.is_valid():
            form.save(commit=True)            
    else:
        form= RestaurantOwnerSignupForm()
    return render(response,"user/creator_signup.html",{'form':form})
def profile(response):
    user = get_user(response)
    # if he is a restaurant owner
    is_creator = user.groups.contains(Restaurant_owner_group.group())
    # print(user.groups)
    return render(response,'user/profile.html',{
        'is_creator' : is_creator,
        'user':user
    })
def creator_page(response):
    return render(response,'user/creator_page.html')

