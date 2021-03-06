# -*- coding: utf-8 -*-

import sqlite3
import json


class StockEntity:
    # Database entity for stock
    def __init__(self) -> None:

        # open a connection to database
        self.con = sqlite3.connect('stock.db')

        # open a cursor to perform operations
        self.cur = self.con.cursor()

        self.setup()

        print("Successfully connected to stock.db")

    def read(self, name=None) -> list:
        # Read stocks with given name. If name is `None`, then return all records from table.

        try:
            sql = "SELECT name, actualqty, minqty FROM stocks " + \
                ("" if name is None else (" WHERE name = '" + name + "'"))
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            return list(rows)
        except Exception as exp:
            print("Exception while reading data: ")
            print(exp)
            return []

    def write(self, name, actualQty, minQty) -> bool:
        # Insert a new record to the stocks table. Return False if stock with same name already exists

        existing = self.read(name)
        if len(existing) > 0:
            print("Stock " + name + " already exists")
            return False
        self.cur.execute("insert into stocks (name, actualqty, minqty) values (?, ?, ?)",
                         (name, float(actualQty), float(minQty)))
        self.con.commit()
        return True

    def update(self, name, actualQty=None, minQty=None) -> bool:
        # Update an existing stocks record. Return False if no unique record with same name exists.

        if actualQty is None or minQty is None:
            existing = self.read(name)
            if len(existing) != 1:
                print("Stock " + name + " not found")
                return False
            existing = existing[0]
            if minQty is None:
                minQty = existing[2]
            if actualQty is None:
                actualQty = existing[1]
        self.cur.execute("update stocks set actualqty = " + str(actualQty) + ", minQty = " + str(minQty) +
                         " where name = '" + name + "'")
        self.con.commit()
        return True

    def setup(self):
        # check if table exists or not already

        try:
            self.cur.execute(
                '''CREATE TABLE stocks (stock_id integer primary key autoincrement, name text unique, actualqty real, minqty real)''')
        except Exception as exp:
            print(exp)

    def __exit__(self, exc_type, exc_value, traceback):
        # When object is destroyed, then close the cursor and db connection

        self.cur.close()
        self.con.close()


class ProductEntity:
    # Database entity for product
    def __init__(self) -> None:

        # open a connection to database
        self.con = sqlite3.connect('product.db')

        # open a cursor to perform operations
        self.cur = self.con.cursor()

        self.setup()

        print("Successfully connected to product.db")

    def read(self, name=None) -> list:
        # Read products with given name. If name is `None`, then return all records from table.

        try:
            sql = "SELECT name, actualqty, minqty, component_list FROM products " + \
                ("" if name is None else (" WHERE name = '" + name + "'"))
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            return list(rows)
        except Exception as exp:
            print("Exception while reading data: ")
            print(exp)
            return []

    def write(self, name, actualQty, minQty, componentList) -> bool:
        # Insert a new record to the products table. Return False if product with same name already exists

        existing = self.read(name)
        if len(existing) > 0:
            print("Product " + name + " already exists")
            return False
        self.cur.execute("insert into products (name, actualqty, minqty, component_list) values (?, ?, ?, ?)",
                         (name, float(actualQty), float(minQty), json.dumps(componentList)))
        self.con.commit()
        return True

    def update(self, name, actualQty=None, minQty=None, componentList=None) -> bool:
        # Update an existing stocks record. Return False if no unique record with same name exists.

        if actualQty is None or minQty is None or componentList is None:
            existing = self.read(name)
            if len(existing) != 1:
                print("Product " + name + " not found")
                return False
            existing = existing[0]
            if minQty is None:
                minQty = existing[2]
            if actualQty is None:
                actualQty = existing[1]
            if componentList is None:
                componentList = existing[3]
        self.cur.execute("update products set actualqty = " + str(actualQty) + ", minQty = " + str(
            minQty) + ", component_list = '" + json.dumps(componentList) + "'" + " where name = '" + name + "'")
        self.con.commit()
        return True

    def setup(self):
        # check if table exists or not already

        try:
            self.cur.execute(
                '''CREATE TABLE products (product_id integer primary key autoincrement, name text unique, actualqty real, minqty real, component_list text)''')
        except Exception as exp:
            print(exp)

    def __exit__(self, exc_type, exc_value, traceback):
        # When object is destroyed, then close the cursor and db connection

        self.cur.close()
        self.con.close()
