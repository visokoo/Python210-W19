"""
InventoryCount class
"""

from Product import Product


class InventoryCount(object):
    def __init__(self, product: Product, product_inventory_count: int):
        self.__product = product
        self.__product_inventory_count = product_inventory_count

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product: str):
        self.__product = self.__product.strip()

    @property
    def product_inventory_count(self):
        return self.__product_inventory_count

    @product_inventory_count.setter
    def product_inventory_count(self, product_inventory_count: int):
        if type(product_inventory_count) is not int:
            raise Exception("Product Inventory count must be an int.")
        else:
            self.__product_inventory_count = product_inventory_count

    def __str__(self):
        return f"Product [{self.__product}] | Inventory Count: {self.__product_inventory_count}"

    def __dict__(self):
        return {
            "Product ID": self.__product.product_id,
            "Product Name": self.__product.product_name,
            "Inventory Count": self.__product_inventory_count
        }

    def __repr__(self):
        return f"Inventory Count:[{self.__dict__()}]"


if __name__ == '__main__':
    p1 = Product(1, "Mouse")
    p2 = Product(2, "Keyboard")
    i1 = InventoryCount(p1, 2)
    i2 = InventoryCount(p2, 40)
    print(i1)
    print(i2)
