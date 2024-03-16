from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    # password?

class DeliveryCrew(models.Model):
    username = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

class MenuItem(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    featured = models.BooleanField(default=False)
    # many items to one category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name
  


class Order(models.Model):
    delivery_status = models.BooleanField()
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(DeliveryCrew, on_delete=models.PROTECT, default=1)