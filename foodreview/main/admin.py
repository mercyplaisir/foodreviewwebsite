from django.contrib import admin
from .models import Restaurant,Customer,Review
# Register your models here.
admin.site.register([Restaurant,Customer,Review])