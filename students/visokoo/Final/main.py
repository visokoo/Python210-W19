"""
main module to run the app
"""

from libs.DBProcessor import DBProcessor
from libs.ProductsProcessor import ProductProcessor
from libs.InventoryCountProcessor import InventoryCountProcessor
from libs.InventoryProcessor import InventoryProcessor

product = ProductProcessor(db_con="visokoo", db_name="visokoo_test.db")
inventory = InventoryProcessor(db_con="visokoo", db_name="visokoo_test.db")
inventorycounts = InventoryCountProcessor(
    db_con="visokoo", db_name="visokoo_test.db")
products_table = product.create_table()
inventory_table = inventory.create_table()
inventory_counts_table = inventorycounts.create_table()
products_table_insert = product.create_insert_statement({
    "productid": "1",
    "productname": "doll"
})
inventory_table_insert = inventory.create_insert_statement({
    "inventoryid":
    "1",
    "inventorydate":
    "2019-02-01"
})
inventory_counts_table_insert = inventorycounts.create_insert_statement({
    "productid":
    "1",
    "inventoryid":
    "1",
    "count":
    "1"
})
# select_statement = product.create_select_statement("products", "*")
product.execute_sql(products_table)
product.execute_sql(products_table_insert)
inventory.execute_sql(inventory_table)
inventory.execute_sql(inventory_table_insert)
inventorycounts.execute_sql(inventory_counts_table)
inventorycounts.execute_sql(inventory_counts_table_insert)
# csr = product.execute_sql(select_statement)
# for row in csr:
#     print(row)
