from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    """"""
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Restaurant(models.Model):
    """"""
    creator = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Review(models.Model):
    """"""
    customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    star =  models.CharField(max_length=1,default='')
    comment = models.CharField(max_length=2000,default='')

    def __str__(self) -> str:
        return f"""{self.customer.username} -to - {self.restaurant.name} \n
                    star:{self.star} \n
                    comment:{self.comment}"""

