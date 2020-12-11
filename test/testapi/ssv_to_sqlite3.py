from pathlib import Path
import sys
import os

BASE_DIR = Path(__file__).resolve().parent
csv_filepathname = BASE_DIR / "data_productsale.csv"
sys.path.append(BASE_DIR.parent.parent)
os.environ['DJANGO_SETTINGS_MODULE'] = 'test.settings'
print(BASE_DIR.parent.parent)

import csv
from test.testapi.models import Shop, Product, Sales


def parse_csv():
    dataReader = csv.reader(open(csv_filepathname), delimiter=',')

    old_school = None
    for row in dataReader:
        id = row[0]
        shop = Shop()
        shop.shop_id = id
        shop.save()

    dataReader = csv.reader(open(csv_filepathname), delimiter=',')

    for row in dataReader:
        product = Product()
        product.product_id = row[1]
        shop_id = Shop.objects.get(shop_id=row[0])
        product.shop_id = shop_id
        product.save()

    dataReader = csv.reader(open(csv_filepathname), delimiter=',')

    for row in dataReader:
        sales = Sales()
        sales.qty = row[3]
        product_id = Product.objects.get(product_id=row[2])
        sales.product_id = product_id
        sales.save()


parse_csv()

