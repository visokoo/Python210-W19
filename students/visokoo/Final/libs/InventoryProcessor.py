"""
InventoryProcessor class
"""

from .DBProcessor import *


class InventoryProcessor(DBProcessor):
    table_name = "inventories"
    columns = {
        "InventoryID": "primary key not null",
        "InventoryDate": "date not null"
    }
