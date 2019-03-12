"""
Inventory class
"""


class Inventory(object):
    def __init__(self, inventory_id, inventory_count, inventory_date):
        self.inventory_id = inventory_id
        self.inventory_count = inventory_count
        self.inventory_date = inventory_date