# -*- coding: utf-8 -*-

# Mood-Changing-Items
# Tabel to connect items and moods with effects

import logging
# for DB usage
import sqlite3

logging.basicConfig(filename='log.txt',level=logging.DEBUG) 

#mood
def make_tabel_mood_changing_item():
    try:
        con = sqlite3.connect('game.db')
        con.execute('''CREATE TABLE IF NOT EXISTS mood_changing_item (
            id INTEGER PRIMARY KEY, 
            mood CHAR(100) NOT NULL, 
            item INT, 
            effect INT 
            )
            ''') 
        con.commit()
        con.close()
    except Exception as msg:
        print('make_tabel_mood_changing_item: ERROR: ', msg)
        logging.debug('make_tabel_mood_changing_item: ERROR: ', msg)
        print(msg)

#make_tabel_mood_changing_item()

def write_tabel_mood_changing_item(data):
    mood, item, effect = data
    try: 
        con = sqlite3.connect('game.db')
        con.execute('INSERT INTO mood_changing_item (mood, item, effect) VALUES (?,?,?);',(mood, item, effect))
        con.commit()
    except Exception as msg:
        print(msg)
        #logging.debug('write_tabel_mood_changing_item: Error', msg)
    finally:
        if con:
            con.close()

            
# make mood_changing_items

# Hungry-mood:
#write_tabel_mood_changing_item(('hungry', 'Berry',18000))
#write_tabel_mood_changing_item(('hungry', 'Raspberry', 36000))
#write_tabel_mood_changing_item(('hungry', 'Sandwich', 216000))
#write_tabel_mood_changing_item(('hungry', 'Melon', 234000))
#write_tabel_mood_changing_item(('hungry', 'Chocolate', 15336000))

def alter_tabel_mood_changing_item(data_name,data_content):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE mood_changing_item SET {}={};".format(data_name, data_content) # image_path CHAR(200)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_mood_changing_item: ERROR: ', msg)
    finally:
        if con:
            con.close()


def alter_tabel_mood_changing_item_where(data_name, data_content, where, what):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE mood_changing_item SET {}='{}' WHERE {}='{}';".format(data_name, data_content, where, what)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_mood_changing_item_where: ERROR: ', msg)
        logging.debug('alter_tabel_mood_changing_item_where: ERROR:', msg)
    finally:
        if con:
            con.close()

#alter_tabel_mood_changing_item_where('item', 'Berry', 'effect', 15000)

def read_everything_from_tabel_mood_changing_item():
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT * FROM mood_changing_item"
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        logging.debug("read_everything_from_tabel_mood_changing_item: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_everything_from_tabel_mood_changing_item: ERROR:', msg)
    finally:
        if con:
            con.close()
#mood_changing_items = read_everything_from_tabel_mood_changing_item()
#print(mood_changing_items)

def read_value_from_tabel_mood_changing_item(value, where, what):
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT {} FROM mood_changing_item WHERE {}='{}';".format(value, where, what)
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        logging.debug("read_value_from_tabel_mood_changing_item: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_value_from_tabel_mood_changing_item: ERROR:', msg)
    finally:
        if con:
            con.close()

def read_from_tabel_mood_changing_item(value, where, what):
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT {} FROM mood_changing_item WHERE {};".format(value, where)
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        logging.debug("read_value_from_tabel_mood_changing_item: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_value_from_tabel_mood_changing_item: ERROR:', msg)
    finally:
        if con:
            con.close()
