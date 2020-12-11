from rest_framework import serializers
from .models import Shop, Product, Sales
import pandas as pd


def ABC_segmentation(perc):
    if perc > 0 and perc < 60:
        return 'A'
    elif perc >= 60 and perc < 85:
        return 'B'
    elif perc >= 85:
        return 'C'


def my_abc(products):
    pd_arr = []
    for p in products:
        sales = Sales.objects.get(product_id=p)
        pd_arr.append(sales.qty)
    abc = pd.Series(pd_arr)  # create series
    max = abc.max()  # max value in series
    abc = abc.apply(lambda x: (x * 100) / max)  # create series interest
    abc = abc.apply(ABC_segmentation)  # abc
    return abc


def get_json(id=-1):
    if id == -1:
        rez = []
        shops = Shop.objects.all()
        for s in shops:
            products = Product.objects.filter(shop_id=s)

            abc = my_abc(products)

            pr = []
            for i in range(0, len(products)):
                pri = {products[i].product_id: abc[i]}
                pr.append(pri)
            r = {s.shop_id: pr}
            rez.append(r)
        return rez
    else:
        shop = Shop.objects.get(shop_id=id)
        products = Product.objects.filter(shop_id=shop)

        abc = my_abc(products)

        pr = []
        for i in range(0, len(products)):
            pri = {products[i].product_id: abc[i]}
            pr.append(pri)
        r = {shop.shop_id: pr}
        return r


class ShopSerializer(serializers.Serializer):
    shop_id = serializers.IntegerField()

    product_id = serializers.SerializerMethodField()

    def get_product_id(self, obj):
        products = Product.objects.filter(shop_id=obj)
        sales1 = Sales.objects.get(product_id=products[0])
        return sales1.qty
