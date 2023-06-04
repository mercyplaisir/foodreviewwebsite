from django.urls import path
from . import views


urlpatterns = [
    
    path("create/",views.restaurant_create, name="restaurant creation"),
    path('<str:name>/',views.restaurant_page),
]
