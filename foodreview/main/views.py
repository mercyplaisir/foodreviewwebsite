from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User

from .models import Restaurant,Review
from .forms import CreateNewReviews
# Create your views here.
def index(response):
    user = response.user
    return render(response,"main/base.html" ,{'user':user})

def homepage(response):
    restaurants = Restaurant.objects.all()
    
    return render(response,"main/home.html",{'restaurants': restaurants})

def restaurant_page(response,id:int):
    restaurant = Restaurant.objects.get(id=id)
    reviews = restaurant.review_set.all()
    if response.method == 'POST':
        form = CreateNewReviews(response.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            stars = form.cleaned_data['stars']
            
            rev = Review(customer = response.user,
                        restaurant = restaurant,
                        star = stars[0],
                        comment=comment)
            rev.save()
    form = CreateNewReviews()
    return render(response,"main/restaurant.html",
                {'reviews': reviews,
                'restaurant':restaurant,
                'form':form})

def customer_page(response,id:int):
    customer = Customer.objects.get(id=id)
    return