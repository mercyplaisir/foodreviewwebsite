from django.shortcuts import render
from .forms import SignupForm
# Create your views here.

def login_page(response):
    return render(response,"user/login.html")

def signup_page(response):
    if response.method == "POST":
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form= SignupForm()
    return render(response,"user/signup.html",{'form':form})
