# Techdegree Project 4

from peewee import *
import datetime
import csv


db = SqliteDatabase('inventory.db')

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
                    product_quantity = int(value)
                if key == "product_price":
                    product_price = float(value.replace("$", ""))
                if key == "date_updated":
                    date_updated = datetime.datetime

        print(row)

if __name__ == "__main__":
    db.connect()
    db.create_tables([Product], safe=True)
    inventory()

