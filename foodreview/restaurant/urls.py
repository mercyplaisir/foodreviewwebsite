from django.urls import path
from . import views

from main.utils import create_group
from .groups import Restaurant_owner

urlpatterns = [
    
    path('<str:name>',views.restaurant_page)
]


#create group
create_group(name = Restaurant_owner.name,
             model = Restaurant_owner.model,
             perm= Restaurant_owner.perm)