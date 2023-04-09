from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer,Restaurant,Review

# Create your views here.
def homepage(response):
    return HttpResponse("<h1>WELCOME</h1>")

def restaurant_page(response,id:int):
    restaurant = Restaurant.objects.get(id=id)
    review = restaurant.review_set.get(id=id)
    return HttpResponse(f"<h1>{restaurant.name}</h1>\b{review}")

def customer_page(response,id:int):
    customer = Customer.objects.get(id=id)
    return