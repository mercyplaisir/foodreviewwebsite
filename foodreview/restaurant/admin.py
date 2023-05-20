from django.contrib import admin
from .models import Restaurant
from .models import Restaurant_address
# Register your models here.
admin.site.register(
    [Restaurant,
     Restaurant_address]
)