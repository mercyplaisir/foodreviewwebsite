from django.urls import path
from . import views

from django.urls import path, include

urlpatterns = [
    path('signup/', views.signup_page,name= "userSignup" ),
    
    path('',include("django.contrib.auth.urls")),
    path('',views.profile)
]