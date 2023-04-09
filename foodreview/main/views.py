from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer,Restaurant,Review

# Create your views here.
def index(response):
    return render(response,"main/base.html" ,{})

def homepage(response):
    restaurants = Restaurant.objects.all()
    return render(response,"main/home.html",{'restaurants': restaurants})

def restaurant_page(response,id:int):
    restaurant = Restaurant.objects.get(id=id)
    reviews = restaurant.review_set.all()
    return render(response,"main/restaurant.html",{'reviews': reviews,'restaurant':restaurant})

def customer_page(response,id:int):
    customer = Customer.objects.get(id=id)
    return