"""
main module to run the app
"""
import DBProcessor as dp
import Product as pr
import Inventory as ir
import InventoryCount as ic
from tkinter import ttk
import logging
import tkinter as tk


class MainWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title = "Inventory Manager"
        self.window['padx'] = 10
        self.window['pady'] = 10
        self.notebook = ttk.Notebook(self.window)
        self.configure_notebook_tabs(self.notebook)

    @staticmethod
    def redirector(text_box, output):
        text_box.insert(tk.END, output)

    def configure_notebook_tabs(self, notebook_tabs):
        notebook_tabs.grid(row=4, column=2, padx=20, pady=10)
        self.products_tabs(notebook_tabs)
        self.inventory_tabs(notebook_tabs)
        self.inventory_count_tabs(notebook_tabs)
        self.quit_button()
        return notebook_tabs

    def quit_button(self):
        btn_quit = ttk.Button(
            self.window, text="Quit", command=self.window.quit)
        btn_quit.grid(row=7, column=2)

    def products_tabs(self, notebook_tabs):
        products_tab = tk.Frame(notebook_tabs)
        notebook_tabs.add(products_tab, text="Products", compound=tk.TOP)

        mtx_instructions = tk.Text(
            products_tab, width=50, height=10, borderwidth=2, relief='ridge')
        mtx_instructions.grid(row=6, column=2, sticky=tk.W)
        mtx_instructions.insert(
            tk.END, """Instructions:\n
Select: Returns all data in textbox\n
Insert: Fill in all values except Filter\n
Update: Fill in all values and type in the row ID for Filter\n
Delete: Fill in the row ID for Filter
                """)

        lbl_product_id = ttk.Label(
            products_tab, text="Product ID", width=20, anchor=tk.E)
        lbl_product_id.grid(row=2, column=2, sticky=tk.E)
        txt_product_id = ttk.Entry(products_tab, width=20)
        txt_product_id.grid(row=2, column=3, columnspan=2, sticky=tk.E)
        txt_product_id.insert(0, "<product id>")

        lbl_product_name = ttk.Label(
            products_tab, text="Product Name", width=20, anchor=tk.E)
        lbl_product_name.grid(row=3, column=2, sticky=tk.E)
        txt_product_name = ttk.Entry(products_tab, width=20)
        txt_product_name.grid(row=3, column=3, columnspan=2, sticky=tk.E)
        txt_product_name.insert(0, "<product name>")

        lbl_product_filter = ttk.Label(
            products_tab, text="Primary ID Filter", width=20, anchor=tk.E)
        lbl_product_filter.grid(row=4, column=2, sticky=tk.E)
        txt_product_filter = ttk.Entry(products_tab, width=20)
        txt_product_filter.grid(row=4, column=3, columnspan=2, sticky=tk.E)
        txt_product_filter.insert(0, "<primary id>")

        mtx = tk.Text(
            products_tab, width=40, height=10, borderwidth=2, relief='ridge')
        mtx.grid(row=6, column=0, sticky=tk.W)

        table = "products"

        btn_sel_product_info = ttk.Button(
            products_tab,
            text="Select Product Info",
            command=lambda: IOProcessor.sel(table, mtx, "products"))
        btn_sel_product_info.grid(row=1, column=0)

        btn_ins_product_info = ttk.Button(
            products_tab,
            text="Insert Product Info",
            command=lambda: IOProcessor.ins_product(
                table, mtx, ttk.Entry.get(txt_product_id),
                ttk.Entry.get(txt_product_name)))
        btn_ins_product_info.grid(row=2, column=0)

        btn_upd_product_info = ttk.Button(
            products_tab,
            text="Update Product Info",
            command=lambda: IOProcessor.upd_product(
                table, mtx, ttk.Entry.get(txt_product_id),
                ttk.Entry.get(txt_product_name),
                ttk.Entry.get(txt_product_filter)))
        btn_upd_product_info.grid(row=3, column=0)

        btn_del_product_info = ttk.Button(
            products_tab,
            text="Delete Product Info",
            command=lambda: IOProcessor.del_product(
                table, mtx, ttk.Entry.get(txt_product_id),
                ttk.Entry.get(txt_product_name),
                ttk.Entry.get(txt_product_filter)))
        btn_del_product_info.grid(row=4, column=0)

    def inventory_tabs(self, notebook_tabs):
        inventory_tab = tk.Frame(notebook_tabs)
        notebook_tabs.add(inventory_tab, text="Inventory", compound=tk.TOP)

        mtx_instructions = tk.Text(
            inventory_tab, width=50, height=10, borderwidth=2, relief='ridge')
        mtx_instructions.grid(row=6, column=2, sticky=tk.W)
        mtx_instructions.insert(
            tk.END, """Instructions:\n
Select: Returns all data in textbox\n
Insert: Fill in all values except Filter\n
Update: Fill in all values and type in the row ID for Filter\n
Delete: Fill in the row ID for Filter
                """)

        lbl_inventory_id = ttk.Label(
            inventory_tab, text="Inventory ID", width=20, anchor=tk.E)
        lbl_inventory_id.grid(row=2, column=2, sticky=tk.E)
        txt_inventory_id = ttk.Entry(inventory_tab, width=20)
        txt_inventory_id.grid(row=2, column=3, columnspan=2, sticky=tk.E)
        txt_inventory_id.insert(0, "<inventory id>")

        lbl_inventory_date = ttk.Label(
            inventory_tab, text="Inventory Date", width=20, anchor=tk.E)
        lbl_inventory_date.grid(row=3, column=2, sticky=tk.E)
        txt_inventory_date = ttk.Entry(inventory_tab, width=20)
        txt_inventory_date.grid(row=3, column=3, columnspan=2, sticky=tk.E)
        txt_inventory_date.insert(0, "<inventory date>")

        lbl_inventory_filter = ttk.Label(
            inventory_tab, text="Primary ID Filter", width=20, anchor=tk.E)
        lbl_inventory_filter.grid(row=4, column=2, sticky=tk.E)
        txt_inventory_filter = ttk.Entry(inventory_tab, width=20)
        txt_inventory_filter.grid(row=4, column=3, columnspan=2, sticky=tk.E)
        txt_inventory_filter.insert(0, "<primary id>")

        mtx = tk.Text(
            inventory_tab, width=40, height=10, borderwidth=2, relief='ridge')
        mtx.grid(row=6, column=0, sticky=tk.W)
        table = "inventories"

        btn_sel_inventory_info = ttk.Button(
            inventory_tab,
            text="Select Inventory Info",
            command=lambda: IOProcessor.sel(table, mtx, "inventory"))
        btn_sel_inventory_info.grid(row=1, column=0)

        btn_ins_inventory_info = ttk.Button(
            inventory_tab,
            text="Insert Inventory Info",
            command=lambda: IOProcessor.ins_inventory(
                table, mtx, ttk.Entry.get(txt_inventory_id),
                ttk.Entry.get(txt_inventory_date)))
        btn_ins_inventory_info.grid(row=2, column=0)

        btn_upd_inventory_info = ttk.Button(
            inventory_tab,
            text="Update Inventory Info",
            command=lambda: IOProcessor.upd_inventory(
                table, mtx, ttk.Entry.get(txt_inventory_id),
                ttk.Entry.get(txt_inventory_date),
                ttk.Entry.get(txt_inventory_filter)))
        btn_upd_inventory_info.grid(row=3, column=0)

        btn_del_inventory_info = ttk.Button(
            inventory_tab,
            text="Delete Inventory Info",
            command=lambda: IOProcessor.del_inventory(
                table, mtx, ttk.Entry.get(txt_inventory_id),
                ttk.Entry.get(txt_inventory_date),
                ttk.Entry.get(txt_inventory_filter)))
        btn_del_inventory_info.grid(row=4, column=0)

    def inventory_count_tabs(self, notebook_tabs):
        inventory_count_tab = tk.Frame(notebook_tabs)
        notebook_tabs.add(
            inventory_count_tab, text="Inventory Count", compound=tk.TOP)

        mtx_instructions = tk.Text(
            inventory_count_tab,
            width=50,
            height=10,
            borderwidth=2,
            relief='ridge')
        mtx_instructions.grid(row=6, column=2, sticky=tk.W)
        mtx_instructions.insert(
            tk.END, """Instructions:\n
Select: Returns all data in textbox\n
Insert: Fill in all values except Filter\n
Update: Fill in all values and type in the row ID for Filter\n
Delete: Fill in the row ID for Filter
                """)

        lbl_inventory_id = ttk.Label(
            inventory_count_tab, text="Inventory ID", width=20, anchor=tk.E)
        lbl_inventory_id.grid(row=2, column=2, sticky=tk.E)
        txt_inventory_id = ttk.Entry(inventory_count_tab, width=20)
        txt_inventory_id.grid(row=2, column=3, columnspan=2, sticky=tk.E)
        txt_inventory_id.insert(0, "<inventory id>")

        lbl_inventory_count = ttk.Label(
            inventory_count_tab, text="Inventory Count", width=20, anchor=tk.E)
        lbl_inventory_count.grid(row=3, column=2, sticky=tk.E)
        txt_inventory_count = ttk.Entry(inventory_count_tab, width=20)
        txt_inventory_count.grid(row=3, column=3, columnspan=2, sticky=tk.E)
        txt_inventory_count.insert(0, "<inventory count>")

        lbl_product_id = ttk.Label(
            inventory_count_tab, text="Product ID", width=20, anchor=tk.E)
        lbl_product_id.grid(row=4, column=2, sticky=tk.E)
        txt_product_id = ttk.Entry(inventory_count_tab, width=20)
        txt_product_id.grid(row=4, column=3, columnspan=2, sticky=tk.E)
        txt_product_id.insert(0, "<product id>")

        lbl_inventory_count_filter = ttk.Label(
            inventory_count_tab,
            text="Primary ID Filter",
            width=20,
            anchor=tk.E)
        lbl_inventory_count_filter.grid(row=5, column=2, sticky=tk.E)
        txt_inventory_count_filter = ttk.Entry(inventory_count_tab, width=20)
        txt_inventory_count_filter.grid(
            row=5, column=3, columnspan=2, sticky=tk.E)
        txt_inventory_count_filter.insert(0, "<primary id>")

        mtx = tk.Text(
            inventory_count_tab,
            width=40,
            height=10,
            borderwidth=2,
            relief='ridge')
        mtx.grid(row=7, column=0, sticky=tk.W)
        table = "inventorycounts"

        btn_sel_inventory_count_info = ttk.Button(
            inventory_count_tab,
            text="Select Inventory Count Info",
            command=lambda: IOProcessor.sel(table, mtx, "inventorycounts"))
        btn_sel_inventory_count_info.grid(row=1, column=0)

        btn_ins_inventory_count_info = ttk.Button(
            inventory_count_tab,
            text="Insert Inventory Count Info",
            command=lambda: IOProcessor.ins_inventory_count(
                table, mtx, ttk.Entry.get(txt_inventory_id),
                ttk.Entry.get(txt_product_id),
                ttk.Entry.get(txt_inventory_count)))
        btn_ins_inventory_count_info.grid(row=2, column=0)

        btn_upd_inventory_count_info = ttk.Button(
            inventory_count_tab,
            text="Update Inventory Count Info",
            command=lambda: IOProcessor.upd_inventory_count(
                table, mtx, ttk.Entry.get(txt_inventory_id),
                ttk.Entry.get(txt_product_id),
                ttk.Entry.get(txt_inventory_count),
                ttk.Entry.get(txt_inventory_count_filter)))
        btn_upd_inventory_count_info.grid(row=3, column=0)

        btn_del_inventory_count_info = ttk.Button(
            inventory_count_tab,
            text="Delete Inventory Count Info",
            command=lambda: IOProcessor.del_inventory_count(
                table, mtx, ttk.Entry.get(txt_inventory_id),
                ttk.Entry.get(txt_inventory_id), ttk.Entry.get(txt_product_id),
                ttk.Entry.get(txt_inventory_count_filter)))
        btn_del_inventory_count_info.grid(row=4, column=0)


class IOProcessor():
    @staticmethod
    def sel(table, text_box, processor):
        try:
            select_statement = dp.DBProcessor.create_select_statement(
                table, "*")
            output = db.execute_sql(select_statement)
            MainWindow.redirector(text_box, select_statement + "\n")
            obj = []
            for data in output:
                if processor == "products":
                    obj.append(pr.Product(data[0], data[1]))
                elif processor == "inventory":
                    obj.append(ir.Inventory(data[0], data[1]))
                elif processor == "inventorycounts":
                    obj.append(ir.InventoryCount(data[0], data[1]))
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
                MainWindow.redirector(text_box, obj)
                MainWindow.redirector(text_box, "\n")

        except Exception as e:
            MainWindow.redirector(text_box, e)

    @staticmethod
    def ins_product(table, text_box, id, name):
        try:
            data_dict = dict(productid=id, productname=name)
            insert_statement = pp.create_insert_statement(table, data_dict)
            output = pp.execute_sql(insert_statement)
            MainWindow.redirector(text_box, insert_statement + "\n")

            for data in output:
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
        except Exception as e:
            MainWindow.redirector(text_box, e)

    @staticmethod
    def upd_product(table, text_box, id, name, filters):
        try:
            data_dict = dict(productname=name)
            filter_dict = dict(productid=filters)
            update_statement = pp.create_update_statement(
                table, data_dict, filter_dict)
            output = pp.execute_sql(update_statement)
            MainWindow.redirector(text_box, update_statement + "\n")

            for data in output:
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
        except Exception as e:
            MainWindow.redirector(text_box, e)

    @staticmethod
    def del_product(table, text_box, id, name, filters):
        try:
            filter_dict = dict(productid=filters)
            delete_statement = pp.create_delete_statement(table, filter_dict)
            output = pp.execute_sql(delete_statement)
            MainWindow.redirector(text_box, delete_statement + "\n")

            for data in output:
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
        except Exception as e:
            MainWindow.redirector(text_box, e)

    @staticmethod
    def ins_inventory(table, text_box, id, date):
        try:
            data_dict = dict(inventoryid=id, inventorydate=date)
            insert_statement = ip.create_insert_statement(table, data_dict)
            output = ip.execute_sql(insert_statement)
            MainWindow.redirector(text_box, insert_statement + "\n")

            for data in output:
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
        except Exception as e:
            MainWindow.redirector(text_box, e)

    @staticmethod
    def upd_inventory(table, text_box, id, date, filters):
        try:
            data_dict = dict(inventoryid=id, inventorydate=date)
            filter_dict = dict(inventoryid=filters)

            update_statement = ip.create_update_statement(
                table, data_dict, filter_dict)
            output = ip.execute_sql(update_statement)
            MainWindow.redirector(text_box, update_statement + "\n")

            for data in output:
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
        except Exception as e:
            MainWindow.redirector(text_box, e)

    @staticmethod
    def del_inventory(table, text_box, id, date, filters):
        try:
            filter_dict = dict(inventoryid=filters)

            delete_statement = ip.create_delete_statement(table, filter_dict)
            output = ip.execute_sql(delete_statement)
            MainWindow.redirector(text_box, delete_statement + "\n")

            for data in output:
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
        except Exception as e:
            MainWindow.redirector(text_box, e)

    @staticmethod
    def ins_inventory_count(table, text_box, inventory_id, product_id, count):
        try:
            data_dict = dict(
                inventoryid=inventory_id, productid=product_id, inventorycount=count)
            insert_statement = ic.create_insert_statement(table, data_dict)
            output = ic.execute_sql(insert_statement)
            MainWindow.redirector(text_box, insert_statement + "\n")

            for data in output:
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
        except Exception as e:
            MainWindow.redirector(text_box, e)

    @staticmethod
    def upd_inventory_count(table, text_box, inventory_id, product_id, count,
                            filters):
        try:
            data_dict = dict(
                inventoryid=inventory_id,
                productid=product_id,
                inventorycount=count)
            filter_dict = dict(inventoryid=filters)

            update_statement = ic.create_update_statement(
                table, data_dict, filter_dict)
            output = ip.execute_sql(update_statement)
            MainWindow.redirector(text_box, update_statement + "\n")

            for data in output:
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
        except Exception as e:
            MainWindow.redirector(text_box, e)

    @staticmethod
    def del_inventory_count(table, text_box, inventory_id, product_id, count,
                            filters):
        try:
            filter_dict = dict(inventoryid=filters)

            delete_statement = ic.create_delete_statement(table, filter_dict)
            output = ic.execute_sql(delete_statement)
            MainWindow.redirector(text_box, delete_statement + "\n")

            for data in output:
                MainWindow.redirector(text_box, data)
                MainWindow.redirector(text_box, "\n")
        except Exception as e:
            MainWindow.redirector(text_box, e)


if __name__ == '__main__':
    db = dp.DBProcessor(db_con="visokoo", db_name="visokoo.db")
    pp = dp.ProductProcessor(db_con="visokoo", db_name="visokoo.db")
    ip = dp.InventoryProcessor(db_con="visokoo", db_name="visokoo.db")
    ic = dp.InventoryCountProcessor(db_con="visokoo", db_name="visokoo.db")
    product_tbl = pp.create_table()
    inventory_tbl = ip.create_table()
    inventory_count_tbl = ic.create_table()
    try:
        for tbl in product_tbl, inventory_tbl, inventory_count_tbl:
            db.execute_sql(tbl)
    except Exception:
        print("Tables already created, opening the GUI.")

    window = MainWindow()
    window.window.mainloop()
