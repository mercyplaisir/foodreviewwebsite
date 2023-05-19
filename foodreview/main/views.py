from django.shortcuts import render


from restaurant.models import Restaurant
# Create your views here.
def index(response):
    user = response.user
    return render(response,"main/base.html" ,{'user':user})

def homepage(response):
    restaurants = Restaurant.objects.all()
    
    return render(response,"main/home.html",{'restaurants': restaurants})



def customer_page(response,id:int):
    customer = Customer.objects.get(id=id)
    return