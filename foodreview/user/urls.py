from django.urls import path
from django.urls import path, include

from . import views
from .custom.group import instantiate_groups


urlpatterns = [
    path('signup/', views.signup_page,name= "signup_page" ),
    
    path('',include("django.contrib.auth.urls"),name='user_login'),
    path('profile',views.profile,name='user_profile'),
    path("creator_signup",views.restaurant_owner_signup_page,name='restaurant_creator_signup_page'),
    path("creator_page",views.creator_page,name='restaurant_creator_page'),
    path("user_update",views.user_update,name='restaurant_creator_page'),
]

#create groups
instantiate_groups()