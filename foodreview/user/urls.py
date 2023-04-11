from django.urls import path
from . import views

from django.urls import path, include

urlpatterns = [
    path('signup/', views.signup_page,name= "userSignup" ),
    path('login/',views.login_page,name="loginSignup"),
    path("user/",include("django.contrib.auth.urls"))
]