# -*- coding: utf-8 -*-
import logging
# for DB usage
import sqlite3


logging.basicConfig(filename='log.txt',level=logging.DEBUG) 

#Voc
def make_tabel_item():
    try:
        con = sqlite3.connect('game.db')
        con.execute('''CREATE TABLE IF NOT EXISTS item (
            id INTEGER PRIMARY KEY, 
            name CHAR(100) NOT NULL, 
            description CHAR(500) NOT NULL, 
            image INT,
            price INT
            )
            ''') 
        con.commit()
        con.close()
    except Exception as msg:
        print('make_tabel_voc: ERROR: ', msg)
        logging.debug('make_tabel_voc: ERROR: ', msg)
        print(msg)

#make_tabel_item()

def write_tabel_item(data):
    print(data)
    print(len(data))
    name, description, image, price = data
    try: 
        con = sqlite3.connect('game.db')
        con.execute('INSERT INTO item (name, description, image, price) VALUES (?,?,?,?);',(name, description, image, price))
        con.commit()
    except Exception as msg:
        print(msg)
        #logging.debug('write_tabel_item: Error', msg)
    finally:
        if con:
            con.close()
            
# make items
#write_tabel_item(('Berry', 'This red berry makes good food for pets.', 'berry.png', 5))
#write_tabel_item(('Raspberry', 'Raspberry: fresh and tasty.','raspberry.png', 10))
#write_tabel_item(('Sandwich', 'A sandwich made from bread, cheese and salad. Yum!', 'sandwich.png',15))
#write_tabel_item(('Melon', 'A tasty piece of melon.', 'melon.png', 25))
#write_tabel_item(('Chocolate', 'A delicious chocolate bar.', 'chocolate.png', 50))

def alter_tabel_item(data_name,data_content):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE item SET {}={};".format(data_name, data_content) # image_path CHAR(200)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_item: ERROR: ', msg)
    except Exception as msg:
        logging.debug('alter_tabel_item: ERROR:', msg)
    finally:
        if con:
            con.close()


def alter_tabel_item_where(data_name, data_content, where, what):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE item SET {}='{}' WHERE {}={};".format(data_name, data_content, where, what) # image_path CHAR(200)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_item_where: ERROR: ', msg)
        logging.debug('alter_tabel_item_where: ERROR:', msg)
    finally:
        if con:
            con.close()

#alter_tabel_item_where('name', 'malon','price', 30)

def read_everything_from_tabel_item():
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT * FROM item"
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        logging.debug("read_everything_from_tabel_item: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_everything_from_tabel_item: ERROR:', msg)
    finally:
        if con:
            con.close()

def read_value_from_tabel_item(value, where, what):
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT {} FROM item WHERE {}='{}';".format(value, where, what)
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        logging.debug("read_value_from_tabel_item: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_value_from_tabel_item: ERROR:', msg)
    finally:
        if con:
            con.close()

'''id_num_item_clicked=2
item_data_item_clicked = read_value_from_tabel_item('*', 'id', id_num_item_clicked)
print("test1", item_data_item_clicked)
id_num_item_clicked=4
item_data_item_clicked = read_value_from_tabel_item('*', 'id', id_num_item_clicked)
print("test2", item_data_item_clicked)'''
