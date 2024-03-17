from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DeliveryCrew(models.Model):
    username = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class MenuItem(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    featured = models.BooleanField(default=False)
    # many items to one category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #cart = models.ForeignKey(Cart,  null=True, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
  
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(MenuItem)
    quantity = models.SmallIntegerField
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __str__(self):
        return f'{self.user}'

class Order(models.Model):
    delivery_status = models.BooleanField()
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(DeliveryCrew, on_delete=models.PROTECT, default=1)