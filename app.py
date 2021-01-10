# Techdegree Project 4

from collections import OrderedDict
import datetime
import csv
import sys

from peewee import *


db = SqliteDatabase('inventory.db')

class Product(Model):
    product_id = PrimaryKeyField()
    product_name = CharField(max_length=255, unique=True)
    product_quantity = IntegerField()
    product_price = IntegerField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    db.connect()
    db.create_tables([Product], safe=True)

def inventory():
    with open('inventory.csv', newline='') as csvfile:
        products = csv.DictReader(csvfile)
        rows = list(products)
        for row in rows:
            for key, value in row.items():
                if key == "product_quantity":
                    value = int(value)

                if key == "product_price":
                    value = int(float(value.replace("$", "")) * 100)

                if key == "date_updated":
                    value = datetime.datetime.strptime(value, "%m/%d/%Y")



def menu_loop():
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Enter choice: ').lower().strip()

        if choice in menu:
            menu[choice]()


def view_product(view_product=None):
    #get and display a product by its product_id
    """View Product from Inventory"""
    view_product = input( 'Name of product: ' )
    items = Product.select().order_by(Product.product_name.asc())
    if view_product:
       items = items.where(Product.product_name.contains(view_product))

    for item in items:
        print(item.product_name)


def add_product():
    # add a product to the database; prompt user to enter the product's name, quantity, and price
    # process the entered price from a string to an integer (convert to cents)
    """Add Product to Inventory"""
    print("Enter product name. Press 'command+d' when finished.\n")
    item = sys.stdin.read().strip()

    if item:
        if input("Save product? [Yn] ").lower() != 'n':
            Product.create(content=item)
            print("Product Saved!")


def backup():
    #makes back_up of the database and writes it to a .csv file
    """Backup Inventory"""

menu = OrderedDict([
    ('v', view_product),
    ('a', add_product),
    ('b', backup),
])

if __name__ == "__main__":
    initialize()
    inventory()
    menu_loop()



