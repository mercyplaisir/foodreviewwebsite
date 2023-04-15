from django.db import models
from user.models import CustomUser
# Create your models here.

class Restaurant(models.Model):
    """"""
    creator = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Review(models.Model):
    """"""
    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    star =  models.CharField(max_length=1,default='')
    comment = models.CharField(max_length=2000,default='')

    def __str__(self) -> str:
        return f"""{self.customer.username} -to - {self.restaurant.name} \n
                    star:{self.star} \n
                    comment:{self.comment}"""

