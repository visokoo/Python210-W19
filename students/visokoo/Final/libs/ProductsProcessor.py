"""
ProductProcessor class
"""

from .DBProcessor import *


class ProductProcessor(DBProcessor):
    table_name = "products"
    columns = {
        "ProductID": "primary key not null",
        "ProductName": "varchar(100) not null"
    }
