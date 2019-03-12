"""
main module to run the app
"""
import logging
import tkinter
# logging.basicConfig(filename='main.log')

if __name__ == '__main__':
    import DBProcessor as dp
    import Product as pr
    import Inventory as ir
    import InventoryCount as ic

    pp = dp.ProductProcessor(db_con="visokoo", db_name="visokoo_test.db")
    # product = ProductProcessor(db_con="visokoo", db_name="visokoo_test.db")
    # inventory = InventoryProcessor(db_con="visokoo", db_name="visokoo_test.db")
    # inventorycounts = InventoryCountProcessor(
    #     db_con="visokoo", db_name="visokoo_test.db")
    products_table = pp.create_table()
    # inventory_table = inventory.create_table()
    # inventory_counts_table = inventorycounts.create_table()
    products_table_insert = pp.create_insert_statement({
        "productid": "1",
        "productname": "doll"
    })
    # inventory_table_insert = inventory.create_insert_statement({
    #     "inventoryid":
    #     "1",
    #     "inventorydate":
    #     "2019-02-01"
    # })
    # inventory_counts_table_insert = inventorycounts.create_insert_statement({
    #     "productid":
    #     "1",
    #     "inventoryid":
    #     "1",
    #     "count":
    #     "25"
    # })
    select_statement = pp.create_select_statement("products", "*")
    pp.execute_sql(products_table)
    pp.execute_sql(products_table_insert)
    # inventory.execute_sql(inventory_table)
    # inventory.execute_sql(inventory_table_insert)
    # inventorycounts.execute_sql(inventory_counts_table)
    # inventorycounts.execute_sql(inventory_counts_table_insert)
    print(select_statement)
    products_list = []
    csr = pp.execute_sql(select_statement)
    for row in csr:
        print(row)
        products_list.append(pr.Product(row[0], row[1]))

    print(products_list)
