"""
Product class
"""


class Product(object):
    def __init__(self, product_id: int, product_name: str):
        self.__product_id = product_id
        self.__product_name = product_name

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id: int):
        if type(product_id) is not int: raise TypeError("Requires integer!")
        if product_id <= 0:
            raise ValueError("Requires value greater than zero!")
        else:
            self.__product_id = product_id

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name: str):
        self.__product_name = product_name.strip()

    def __str__(self):
        return f"Product ID: {self.__product_id} | Product Name: {self.__product_name}"

    def __dict__(self):
        return {
            "Product ID": self.__product_id,
            "Product Name": self.__product_name
        }

    def __repr__(self):
        return f"Product:[{self.__dict__()}]"


if __name__ == '__main__':
    p1 = Product(100, "Mouse")
    p2 = Product(200, "Keyboard")
    print(p1)
    print(p2)
