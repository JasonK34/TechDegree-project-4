# Techdegree Project 4

from peewee import *
import datetime
import csv


db = SqliteDatabase('inventory.db')

product_quantity_list = []
product_price_list = []
date_updated_list = []

class Product(Model):
    product_id = PrimaryKeyField()
    product_name = TextField(unique=True)
    product_quantity = IntegerField()
    product_price = IntegerField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def inventory():
    with open('inventory.csv', newline='') as csvfile:
        products = csv.DictReader(csvfile)
        rows = list(products)
        for row in rows:
            for key, value in row.items():
                if key == "product_quantity":
                    value = int(value)
                    product_quantity_list.append(value)

                if key == "product_price":
                    value = int(float(value.replace("$", "")) * 100)
                    product_price_list.append(value)

                if key == "date_updated":
                    print(value)
                    value = datetime.datetime.strptime(value, "%m %d %Y")
                    print(value)


if __name__ == "__main__":
    db.connect()
    db.create_tables([Product], safe=True)
    inventory()



