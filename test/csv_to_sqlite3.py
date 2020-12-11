from pathlib import Path
import sys
import os
import django


BASE_DIR = Path(__file__).resolve().parent.parent
csv_filepathname = "data_productsale.csv"
sys.path.append("..")
os.environ['DJANGO_SETTINGS_MODULE'] = 'test.settings'

django.setup()



import csv
from testapi.models import Shop, Product, Sales


def parse_csv():
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar=' ')
    id = None
    for row in dataReader:
        if row[0] == 'shop_id': continue
        else:
            if Shop.objects.filter(shop_id=int(row[0])).count() == 0:
                id = int(row[0])
                shop = Shop()
                shop.shop_id = id
                shop.save()
            if Product.objects.filter(product_id=int(row[1])).count() == 0:
                product = Product()
                product.product_id = int(row[1])
                shop_id = Shop.objects.get(shop_id=int(row[0]))
                product.shop_id = shop_id
                product.save()

            if Sales.objects.filter(product_id=Product.objects.get(product_id=int(row[1]))).count() == 0:
                sales = Sales()
                sales.qty = float(row[2])
                product_id = Product.objects.get(product_id=int(row[1]))
                sales.product_id = product_id
                sales.save()
            else:
                sales = Sales.objects.get(product_id=Product.objects.get(product_id=int(row[1])))
                sales.qty = sales.qty + float(row[2])
                sales.save()

    # dataReader = csv.reader(open(csv_filepathname), delimiter=',')
    #
    # product_id = None
    # for row in dataReader:
    #     if row[0] == 'shop_id': continue
    #     elif Product.objects.filter(product_id=int(row[1])).count() == 0:
    #         product = Product()
    #         product.product_id = int(row[1])
    #         shop_id = Shop.objects.get(shop_id=int(row[0]))
    #         product.shop_id = shop_id
    #         product.save()
    #
    # dataReader = csv.reader(open(csv_filepathname), delimiter=',')
    #
    # for row in dataReader:
    #     if (row[0] == 'shop_id'): continue
    #     sales = Sales()
    #     sales.qty = float(row[2])
    #     product_id = Product.objects.get(product_id=int(row[1]))
    #     sales.product_id = product_id
    #     sales.save()


parse_csv()

