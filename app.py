# Techdegree Project 4

from pewee import *
import os


db = SqliteDatabase('inventory.db')

class Product(Model):
    product_id = 
    product_name = 
    product_quantity = 
    product_price = 
    date_updated = 

    class Meta:
        database = db