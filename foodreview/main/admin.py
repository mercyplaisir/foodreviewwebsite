from django.contrib import admin
from review.models import Review
from restaurant.models import Restaurant

from user.models import CustomUser
from user.custom_user import CustomUserAdmin
# Register your models here.
admin.site.register([Restaurant,Review])
# Register our custom user
admin.site.register(CustomUser, CustomUserAdmin)
