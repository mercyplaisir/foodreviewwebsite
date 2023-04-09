from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.homepage),
    path('restaurant/<int:id>',views.restaurant_page)
]