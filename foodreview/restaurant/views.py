from django.shortcuts import render

from .models import Restaurant


from review.models import Review
from review.forms import CreateNewReviews

# Create your views here.
def restaurant_page(response,name:str):
    restaurant = Restaurant.objects.get(name=name)
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
    return render(response,"restaurant/restaurant.html",
                {'reviews': reviews,
                'restaurant':restaurant,
                'form':form})

def restaurant_profile(response):
    render(response,'restaurant/profile.html')

def restaurant_settings(response):
    render(response,'restaurant/settings.html')

def resaturant_create(response):
    render(response,'restaurant/create.html')