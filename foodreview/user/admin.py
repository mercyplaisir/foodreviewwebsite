from django.contrib import admin

from .models import CustomUser

from .custom_user import CustomUserAdmin
# Register your models here
admin.site.register([CustomUser,
                     ]
                    , CustomUserAdmin)