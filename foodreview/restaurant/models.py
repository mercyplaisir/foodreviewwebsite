from django.db import models
from user.models import CustomUser
# Create your models here.
class Restaurant(models.Model):
    """Restaurant model"""
    creator = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Restaurant_address(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=5)
    postal_code = models.CharField(max_length=10)
