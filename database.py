# -*- coding: utf-8 -*-

import sqlite3

class StockEntity:
    # Database entity for stock
    def __init__(self) -> None:
        
        # open a connection to database
        self.con = sqlite3.connect('stock.db')
        
        # open a cursor to perform operations
        self.cur = self.con.cursor()
        
        self.setup()
        
        print("Successfully connected to stock.db")
    
    def read(self, name = None) -> list:
        # Read stocks with given name. If name is `None`, then return all records from table.
        try:
            sql = "SELECT * FROM stocks " + ("" if name is None else (" WHERE name = '" + name + "'"))
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
        self.cur.execute("insert into stocks values (?, ?, ?)", (name, float(actualQty), float(minQty)))
        self.con.commit()
        return True
    
    def update(self, name, actualQty = None, minQty = None) -> bool:
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
            self.cur.execute('''CREATE TABLE stocks (name text, actualqty real, minqty real)''')
        except Exception as exp:
            print(exp)
    
    def __exit__(self, exc_type, exc_value, traceback):
        # When object is destroyed, then close the cursor and db connection
        self.cur.close()
        self.con.close()
