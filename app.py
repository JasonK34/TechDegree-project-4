# Techdegree Project 4

from peewee import *
import os
import datetime


db = SqliteDatabase('inventory.db')

class Product(Model):
    product_id = CharField(primary_key=True)
    product_name = TextField()
    product_quantity = IntegerField()
    product_price = IntegerField()
    date_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
    
        
        
if __name__ == "__main__":
    db.connect()
    db.create_tables([Product], safe=True)
    
