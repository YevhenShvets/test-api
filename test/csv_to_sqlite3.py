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
    for row in dataReader:
        if(row[0] == 'shop_id'): continue
        id = int(row[0])
        shop = Shop()
        shop.shop_id = id
        shop.save()

        product = Product()
        product.product_id = int(row[1])
        shop_id = Shop.objects.get(shop_id=int(row[0]))
        product.shop_id = shop_id
        product.save()

        sales = Sales()
        sales.qty = float(row[3])
        product_id = Product.objects.get(product_id=float(row[2]))
        sales.product_id = product_id
        sales.save()

    # dataReader = csv.reader(open(csv_filepathname), delimiter=',')
    #
    # for row in dataReader:
    #     if (row[0] == 'shop_id'): continue
    #     product = Product()
    #     product.product_id = int(row[1])
    #     shop_id = Shop.objects.get(shop_id=int(row[0]))
    #     product.shop_id = shop_id
    #     product.save()
    #
    # dataReader = csv.reader(open(csv_filepathname), delimiter=',')
    #
    # for row in dataReader:
    #     if (row[0] == 'shop_id'): continue
    #     sales = Sales()
    #     sales.qty = float(row[3])
    #     product_id = Product.objects.get(product_id=float(row[2]))
    #     sales.product_id = product_id
    #     sales.save()


parse_csv()

