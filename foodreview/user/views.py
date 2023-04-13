import random
import string
from django.shortcuts import render
from .forms import SignupForm
# Create your views here.

def login_page(response):
    return render(response,"user/login.html")

def signup_page(response):
    if response.method == "POST":
        form = SignupForm(response.POST)
        if form.is_valid():
            
            letters = string.ascii_lowercase
            user_n =  ''.join(random.choice(letters) for i in range(10))
            form.cleaned_data['username'] = user_n
            print(form.data)
            form
    else:
        form= SignupForm()
    return render(response,"user/signup.html",{'form':form})
