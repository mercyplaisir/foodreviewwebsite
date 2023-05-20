from django.urls import path
from django.urls import path, include

from . import views



urlpatterns = [
    path('signup/', views.signup_page,name= "userSignup" ),
    
    path('',include("django.contrib.auth.urls")),
    path('',views.profile),
    path("creator_signup",views.restaurant_owner_signup_page)
]

