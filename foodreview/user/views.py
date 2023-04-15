import random
import string
from django.shortcuts import render
from .forms import CustomerSignupForm,CustomerChangeForm
# Create your views here.

def login_page(response):
    return render(response,"user/login.html")

def signup_page(response):
    if response.method == "POST":
        form = CustomerSignupForm(response.POST)
        if form.is_valid():
            
            letters = string.ascii_lowercase
            user_n =  ''.join(random.choice(letters) for i in range(10))
            
            print(form.data)
            form.save()
    else:
        form= CustomerSignupForm()
    return render(response,"user/signup.html",{'form':form})

def profile(response):
    user = response.user
    form = CustomerChangeForm(instance=user)
    return render(response,'user/profile.html',{'form':form})