"""
DB Processor Base class
"""

import sqlite3


class DBProcessor(object):
    table_name = ""
    columns = {}

    def __init__(self, db_con, db_name=":memory:"):
        self.__db_name = db_name
        self.__db_con = self.create_db(self.db_name)

    @property
    def db_name(self):
        return self.__db_name

    @property
    def db_con(self):
        return self.__db_con

    def create_db(self, db_name):
        conn = sqlite3.connect(db_name)
        return conn

    def execute_sql(self, statement):
        db_con = self.db_con
        try:
            with db_con:
                conn = db_con.cursor()
                conn.execute(statement)
        except Exception as e:
            raise Exception(e)
        return conn

    def create_table(self):
        table_name = self.table_name
        columns = self.columns
        col_collection = ""
        p_key = ""
        if columns is None:
            raise Exception("Must provide at least one column.")
        for column, field_def in columns.items():
            if column == "Primary Key":
                p_key = f", {column}({field_def})"
            else:
                col_collection += f"{column} {field_def}, "
        sql_str = f"create table {table_name.capitalize()}({col_collection[:-2]}{p_key});"
        return sql_str

    def create_select_statement(self, table_name, columns=[], filters={}):
        statement = ""
        col_collection = ""
        filter_statement = ""
        if columns is None:
            raise Exception("Must provide at least one column.")
        for column in columns:
            col_collection += f"{column}, "
        col_collection = col_collection[:-2]
        if filters != {}:
            for f, v in filters.items():
                filter_statement += f"{f}='{v}'"
            statement = f"select {col_collection} from {table_name} where {filter_statement};"
        else:
            statement = f"select {col_collection} from {table_name};"
        return statement

    def create_insert_statement(self, columns={}):
        table_name = self.table_name
        statement = ""
        col_collection = ""
        val_collection = ""
        if columns is None:
            raise Exception("Must provide at least one column.")
        for column, value in columns.items():
            col_collection += f"{column}, "
            val_collection += f"'{value}', "
        col_collection = col_collection[:-2]
        val_collection = val_collection[:-2]
        statement = f"insert into {table_name} ({col_collection}) values ({val_collection});"
        return statement

    def create_delete_statement(self, table_name, filters={}):
        statement = ""
        filter_statement = ""
        if filters is None:
            raise Exception("You must provide a filter condition statement.")
        for f, v in filters.items():
            filter_statement += f"{f}='{v}'"
        statement = f"delete from {table_name} where {filter_statement};"
        return statement

    def create_update_statement(self, table_name, columns={}, filters={}):
        statement = ""
        col_collection = ""
        filter_statement = ""
        if columns is None:
            raise Exception("Must provide at least one column.")
        for column, value in columns.items():
            col_collection += f"{column} = '{value}', "
        col_collection = col_collection[:-2]
        if filters is None:
            raise Exception("You must provide a filter condition statement.")
        for f, v in filters.items():
            filter_statement += f"{f}='{v}'"
            statement = f"update {table_name} set {col_collection} where {filter_statement};"
        return statement


# visokoo = DBProcessor(db_con='visokoo', db_name="visokoo_test.db")
# products_table = visokoo.create_table(
#     "products", {
#         "ProductID": "primary key not null",
#         "ProductName": "varchar(100) not null",
#         "InventoryDate": "date not null"
#     })
# products_table_insert = visokoo.create_insert_statement(
#     "products", {
#         "productid": "1",
#         "productname": "doll",
#         "inventorydate": "2019-02-01"
#     })
# select_statement = visokoo.create_select_statement("products", "*")
# visokoo.execute_sql(products_table)
# visokoo.execute_sql(products_table_insert)
# visokoo.execute_sql(select_statement)

# print(
#     visokoo.create_table("inventory", {
#         "InventoryID": "primary key not null",
#         "InventoryDate": "date not null"
#     }))
# print(
#     visokoo.create_table(
#         "products", {
#             "ProductID": "primary key not null",
#             "ProductName": "varchar(100) not null"
#         }))
# print(
#     visokoo.create_table(
#         "inventorycounts", {
#             "InventoryID": "int not null",
#             "ProductID": "int not null",
#             "Count": "int not null",
#             "Primary Key": "InventoryID, ProductID"
#         }))

# print(visokoo.create_select_statement("students2", ["name", "id"]))
# print(
#     visokoo.create_select_statement("students2", "*", {"text": "dropped out"}))
# print(
#     visokoo.create_insert_statement("students", {
#         "inventoryid": "1",
#         "text": "yo"
#     }))
# print(visokoo.create_delete_statement("students2", {"text": "dropped out"}))
# print(
#     visokoo.create_update_statement("students1", {"primary_key": 1},
#                                     {"text": "dropped out"}))
