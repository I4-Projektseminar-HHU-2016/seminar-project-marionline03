# -*- coding: utf-8 -*-
import logging
# for DB usage
import sqlite3

logging.basicConfig(filename='log.txt',level=logging.DEBUG)

#inventory
def make_tabel_inventory(): 
    try:
        con = sqlite3.connect('game.db')
        con.execute('''CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY, 
            item_name CHAR(100) NOT NULL,
            amount INT)
            ''') 
            # add player_id if multiplayer
        con.commit()
        con.close()
    except Exception as msg:
        print('make_tabel_inventory: ERROR: ', msg)

make_tabel_inventory()

def write_tabel_inventory(data):
    item_name, amount = data
    try:
        con = sqlite3.connect('game.db')
        con.execute("INSERT INTO inventory (item_name, amount) VALUES (?, ?);",(item_name, amount)) 
        con.commit()
        con.close()
        #logging.debug("write_tabel_inventory: wrote data: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('write_tabel_inventory: ERROR:', msg)
    finally:
        if con:
            con.close()    

#write_tabel_inventory(('', 0))

def alter_tabel_inventory(data_name, data_content):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE inventory SET {}='{}';".format(data_name, data_content) 
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_inventory_where: ERROR:', msg)
        print(command)
        #logging.debug('alter_tabel_inventory: ERROR:', msg)
    finally:
        if con:
            con.close()

def alter_tabel_inventory_where(data_name, data_content, where, what):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE inventory SET {}='{}' WHERE {}='{}';".format(data_name, data_content, where, what) 
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_inventory_where: ERROR:', msg)
    finally:
        if con:
            con.close()

#alter_tabel_inventory('score', 5)

def read_everything_from_table_inventory():
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT * FROM inventory"
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        #logging.debug("read_everything_from_inventory_table: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_everything_from_inventory_table: ERROR:', msg)
    finally:
        if con:
            con.close()
            
def read_value_from_tabel_inventory(value, where, what):
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT {} FROM inventory WHERE {}='{}';".format(value, where, what)
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        return data
    except Exception as msg:
        print(msg)
        logging.debug('read_value_from_tabel_inventory: ERROR:', msg)
    finally:
        if con:
            con.close()

'''
def delete_amount_zero_rows_from_tabel():
    try:
        con = sqlite3.connect('game.db')
        c = con.cursor()  
        c.execute("DELETE FROM inventory WHERE amount=0;")
    except Exception as msg:
        print(msg)
        logging.debug('delete_amount_zero_rows_from_tabel: ERROR:', msg)
    finally:
        if con:
            con.close()
#delete_amount_zero_rows_from_tabel()            
'''
