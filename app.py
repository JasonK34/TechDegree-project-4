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
                    value = datetime.datetime.strptime(value, "%m/%d/%Y")
                    date_updated_list.append(value)
                    print(value)

def add_data():
    # add the products listed in the inventory file to the database

def menu():
    print("Welcome to the Inventory! \n")
    options = input("Enter a selection: \n",
                    "'v' to view details of a product\n"
                    "'a' to add product\n"
                    "'b' to create a backup\n")

def product_id():
    # get and display a product by its product_id

def add_product():
    # add a product to the database; prompt user to enter the product's name, quantity, and price
    # process the entered price from a string to an integer (convert to cents)

def back_up():
    # makes back_up of the database and writes it to a .csv file



if __name__ == "__main__":
    db.connect()
    db.create_tables([Product], safe=True)
    inventory()
    menu()



