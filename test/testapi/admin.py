from django.contrib import admin

from .models import Shop, Product, Sales
# Register your models here.

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Sales)
