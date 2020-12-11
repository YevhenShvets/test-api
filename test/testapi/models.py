from django.db import models


class Shop(models.Model):
    shop_id = models.IntegerField()


class Product(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_id = models.IntegerField()


class Sales(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.FloatField()
