from typing import Any
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from main.utils import get_group
from restaurant.groups import Restaurant_owner

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name  = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    d_o_b = models.DateField(null=True)
    phone_number = models.DateField(_("phone number"),max_length=30,null=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_restaurant_owner = models.BooleanField(_('restaurant owner'),default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()
    

    def __str__(self):
        return self.email + '|' + self.last_name + ' ' + self.first_name

