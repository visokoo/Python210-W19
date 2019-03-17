"""
test code for DBProcessor.py
"""

from DBProcessor import DBProcessor, ProductProcessor, InventoryCountProcessor, InventoryProcessor
import pytest
import os


def test_init():
    DBProcessor(db_con="visokoo", db_name="visokoo_test.db")
    assert os.listdir(".").count('visokoo_test.db') == 1


def test_create_product_table():
    pp = ProductProcessor(db_con="visokoo", db_name="visokoo.db")
    pp.table_name = "blah_test"
    pp.columns = {
        "ProductID": "primary key not null",
        "ProductName": "varchar(100) not null"
    }
    assert pp.create_table(
    ) == "create table Blah_test(ProductID primary key not null, ProductName varchar(100) not null);"


def test_create_inventory_table():
    ip = InventoryProcessor(db_con="visokoo", db_name="visokoo.db")
    ip.table_name = "blah_test_inv"
    ip.columns = {
        "InventoryID": "primary key not null",
        "InventoryDate": "date not null"
    }
    assert ip.create_table(
    ) == "create table Blah_test_inv(InventoryID primary key not null, InventoryDate date not null);"


def test_create_inventorycounts_table():
    ic = InventoryCountProcessor(db_con="visokoo", db_name="visokoo.db")
    ic.table_name = "blah_test_invcount"
    ic.columns = {
        "InventoryID": "int not null",
        "ProductID": "int not null",
        "InventoryCount": "int not null",
        "Primary Key": "InventoryID, ProductID"
    }
    assert ic.create_table(
    ) == "create table Blah_test_invcount(InventoryID int not null, ProductID int not null, InventoryCount int not null, Primary Key(InventoryID, ProductID));"


def test_select_statement_generator_with_columns():
    pp = ProductProcessor(db_con="visokoo")
    assert pp.create_select_statement(
        pp.table_name,
        pp.columns) == "select ProductID, ProductName from products;"


def test_select_statement_generator_all():
    pp = ProductProcessor(db_con="visokoo")
    assert pp.create_select_statement(pp.table_name,
                                      "*") == "select * from products;"


def test_insert_statement():
    pp = ProductProcessor(db_con="visokoo")
    assert pp.create_insert_statement(
        pp.table_name,
        {"productname": "arya"
         }) == "insert into products (productname) values ('arya');"


def test_insert_statement_without_columns():
    pp = ProductProcessor(db_con="visokoo")
    with pytest.raises(Exception):
        assert pp.create_insert_statement(
            pp.table_name,
            None) == "insert into products (productname) values ('arya');"


def test_delete_statement():
    pp = ProductProcessor(db_con="visokoo")
    assert pp.create_delete_statement(
        pp.table_name,
        {"productid": 1}) == "delete from products where productid='1';"


def test_delete_statement_without_filters():
    pp = ProductProcessor(db_con="visokoo")
    with pytest.raises(Exception):
        assert pp.create_delete_statement(
            pp.table_name,
            None) == "insert into products (productname) values ('arya');"


def test_update_statement():
    pp = ProductProcessor(db_con="visokoo")
    assert pp.create_update_statement(
        pp.table_name, {"productname": "arya"},
        {"productid": 1
         }) == "update products set productname = 'arya' where productid='1';"


def test_update_statement_without_filters():
    pp = ProductProcessor(db_con="visokoo")
    with pytest.raises(Exception):
        assert pp.create_update_statement(
            pp.table_name,
            None) == "insert into products (productname) values ('arya');"
