# Techdegree Project 4

from peewee import *
import os
import datetime
import csv


db = SqliteDatabase('inventory.db')

class Product(Model):
    product_id = CharField(primary_key=True)
    product_name = TextField()
    product_quantity = IntegerField()
    product_price = IntegerField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
    
with open('inventory.csv', newline= '') as csvfile:
    products = csv.DictReader(csvfile)        
    rows = list(products)
    for row in rows[1:3]:
        print(', '.join(row))  

if __name__ == "__main__":
    db.connect()
    db.create_tables([Product], safe=True)
    
