"""
InventoryCountProcessor class
"""

from .DBProcessor import *


class InventoryCountProcessor(DBProcessor):
    table_name = "inventorycounts"
    columns = {
        "InventoryID": "int not null",
        "ProductID": "int not null",
        "Count": "int not null",
        "Primary Key": "InventoryID, ProductID"
    }