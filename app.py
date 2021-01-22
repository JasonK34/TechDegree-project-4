# Techdegree Project 4

#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import csv
import sys
import os

from peewee import *

db = SqliteDatabase('inventory.db')

class Product(Model):
    product_id = PrimaryKeyField()
    product_name = CharField(max_length=255, unique=True)
    product_quantity = IntegerField(default=0)
    product_price = IntegerField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    db.connect()
    db.create_tables([Product], safe=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def inventory():
    with open('inventory.csv') as shopping_list:
        products = csv.DictReader(shopping_list)
        rows = list(products)
        for row in rows:
            row['product_quantity'] = int(row['product_quantity'])
            row['product_price'] = int(float(row['product_price'].replace("$", ""))) * 100
            row['date_updated'] = datetime.datetime.strptime(row['date_updated'], "%m/%d/%Y")

            try:
                Product.create(product_name=row['product_name'],
                               product_quantity=row['product_quantity'],
                               product_price=row['product_price'],
                               date_updated=row['date_updated'])
            except IntegrityError:
                item_record = Product.get(product_name=row['product_name'])
                item_record.quantity = row['product_quantity']
                item_record.price = row['product_price']
                item_record.date = row['date_updated']
                item_record.save()


def menu_loop():
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Enter choice: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()


def view_product():
    #get and display a product by its product_id
    """View Product from Inventory"""
    #user_choice = input( 'Name of product: ' )
    #show_product = Product.select().where(Product.product_name=user_choice)
    #for product in show_product:
        #clear()
        #print(show_product)


def add_product():
    # add a product to the database; prompt user to enter the product's name, quantity, and price
    # process the entered price from a string to an integer (convert to cents)
    """Add Product to Inventory"""
    #add_item = input("Enter item name. Press 'ctrl+d' when finished.\n")
    #if add_item:
        #add_item = sys.stdin.read().strip()
        #with open("inventory.csv", "a") as shopping_list:
            #save_item = input("Save item? [Yn] ")
            #if save_item != 'n':
                #try:
                    #Product.create(add_item = Product.product_name)
                #except IntegrityError:
                    #item_record = Product.get(product_name = Product.product_name)
                    #item_record.name = (add_item = Product.product_name)
                    #item_record.save()
                #print( "Item Saved!" )
            #shopping_list.close()

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



