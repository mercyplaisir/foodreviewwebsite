
from django.shortcuts import render
from .forms import (CustomerSignupForm,
                    CustomerChangeForm,
                    RestaurantOwnerSignupForm,
                    )
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

def profile(response):
    user = response.user
    form = CustomerChangeForm(instance=user)
    return render(response,'user/profile.html',{'form':form})
def restaurant_owner_signup_page(response):
    if response.method == "POST":
        form = RestaurantOwnerSignupForm(response.POST)
        if form.is_valid():
            form.save(commit=True)            
    else:
        form= RestaurantOwnerSignupForm()
    return render(response,"user/creator_signup.html",{'form':form})
