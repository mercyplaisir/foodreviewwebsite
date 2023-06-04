from django.shortcuts import render
from django.contrib.auth import get_user_model,get_user

from .models import Restaurant


from review.models import Review
from review.forms import CreateNewReviews

from .forms import Restaurant_creation_form,Address_input_form

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
    return render(response,'restaurant/profile.html')

def restaurant_settings(response):
    return render(response,'restaurant/settings.html')

# def restaurant_create(response):
#     rest_det = Restaurant_creation_form()
#     addres_cont = Address_input_form()
#     return render(response,'restaurant/create.html',{
#         'restaurant_form':rest_det,
#         'restaurant_address_form':addres_cont
#     }) 
def restaurant_create(response):
    if response.method=='POST':
        rest_form = Restaurant_creation_form(response.POST)
        addr_form = Address_input_form(response.POST)
        if rest_form.is_valid() and addr_form.is_valid():
            
            addr = addr_form.save()
            user= get_user(response)
            rest_form.manual_save(user,addr)
    rest_det = Restaurant_creation_form()
    addres_cont = Address_input_form()
    return render(response,'restaurant/create.html',{
        'restaurant_form':rest_det,
        'restaurant_address_form':addres_cont
    }) 