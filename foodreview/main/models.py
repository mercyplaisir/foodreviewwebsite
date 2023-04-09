from django.db import models

# Create your models here.

class Customer(models.Model):
    """"""
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Restaurant(models.Model):
    """"""
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Review(models.Model):
    """"""
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    star =  models.CharField(max_length=1)
    comment = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f"""{self.customer.name} -to - {self.restaurant.name} \n
                    star:{self.star} \n
                    comment:{self.comment}"""

