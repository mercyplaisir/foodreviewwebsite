from django.contrib import admin

from .models import CustomUser
from .models import Restaurant_owner

from .custom_user import CustomUserAdmin
# Register your models here
admin.site.register([CustomUser,
                     Restaurant_owner]
                    , CustomUserAdmin)