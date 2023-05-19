from django.db import models
from user.models import CustomUser
# Create your models here.
class Restaurant(models.Model):
    """Restaurant model"""
    creator = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name