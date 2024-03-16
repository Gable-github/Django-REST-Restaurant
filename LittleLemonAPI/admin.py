from django.contrib import admin
from .models import User, Category, MenuItem, Cart, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Order)
