"""
Inventory class
"""
from datetime import datetime
from InventoryCount import InventoryCount
from Product import Product


class Inventory(object):
    def __init__(
            self,
            inventory_id: int,
            inventory_date: datetime.date,
            inventory_count: InventoryCount = [None],
    ):
        self.__inventory_id = inventory_id
        if inventory_date != datetime.strptime(
                inventory_date, '%Y-%m-%d').strftime('%Y-%m-%d'):
            raise ValueError("Not a proper date! E.g. '2020-01-01'")
        else:
            self.__inventory_date = inventory_date
        if inventory_count is not [None]:
            self.__inventory_count = inventory_count

    @property
    def inventory_date(self):
        return self.__inventory_date

    @inventory_date.setter
    def inventory_date(self, inventory_date):
        if inventory_date != datetime.strptime(
                inventory_date, '%Y-%m-%d').strftime('%Y-%m-%d'):
            raise TypeError("Not a proper date! E.g. '2020-01-01'")
        else:
            self.__inventory_date = inventory_date

    @property
    def inventory_id(self):
        return self.__inventory_id

    @property
    def inventory_count(self):
        return self.__inventory_count

    def __str__(self):
        return f"Inventory ID: {self.__inventory_id} | Inventory Date: {self.__inventory_date} | Inventory Count [{self.__inventory_count}]"

    def __dict__(self):
        return {
            "Inventory ID": self.__inventory_id,
            "Inventory Date": self.__inventory_date,
            "Product Name": self.__inventory_count.product.product_name,
            "Product ID": self.__inventory_count.product.product_id,
            "Inventory Count": self.__inventory_count.product_inventory_count
        }

    def __repr__(self):
        return f"Inventory:[{self.__dict__()}]"


if __name__ == '__main__':
    p1 = Product(1, "Mouse")
    p2 = Product(2, "Keyboard")
    p3 = Product(3, "Laptop")
    ic1 = InventoryCount(p1, 2)
    ic2 = InventoryCount(p2, 3)
    ic3 = InventoryCount(p3, 5)
    i1 = Inventory(1, "2020-01-02", ic1)
    i2 = Inventory(2, "2018-12-31", ic2)
    i3 = Inventory(3, "2017-06-22", ic3)
    print(i1)
    print(i2)
    print(i3)