"""
Inventory class
"""


class Inventory(object):
    def __init__(self, inventory_counts, inventory_date, inventory_id):
        self.inventory_counts = inventory_counts
        self.inventory_date = inventory_date
        self.inventory_id = inventory_id
