from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.base_user import BaseUserManager

from .forms import CustomerChangeForm,CustomerSignupForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomerSignupForm
    form = CustomerChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email","password")}),
        ("Personal info",{"fields":('first_name','last_name','d_o_b')}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
