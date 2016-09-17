#Mood 
# -*- coding: utf-8 -*-
import logging
# for DB usage
import sqlite3

logging.basicConfig(filename='log.txt',level=logging.DEBUG) 

#mood
def make_tabel_mood():
    try:
        con = sqlite3.connect('game.db')
        con.execute('''CREATE TABLE IF NOT EXISTS mood (
            id INTEGER PRIMARY KEY, 
            name CHAR(100) NOT NULL, 
            max_value INT, 
            current_value INT 
            )
            ''') 
        con.commit()
        con.close()
    except Exception as msg:
        print('make_tabel_mood: ERROR: ', msg)
        logging.debug('make_tabel_mood: ERROR: ', msg)
        print(msg)

#make_tabel_mood()

def write_tabel_mood(data):
    print(data)
    print(len(data))
    name, max_value, current_value = data
    try: 
        con = sqlite3.connect('game.db')
        con.execute('INSERT INTO mood (name, max_value, current_value) VALUES (?,?,?);',(name, max_value, current_value))
        con.commit()
    except Exception as msg:
        print(msg)
        #logging.debug('write_tabel_mood: Error', msg)
    finally:
        if con:
            con.close()
            
# make moods
#write_tabel_mood(('normal', 0, 0))
#write_tabel_mood(('sleepy', 000, 100))
#write_tabel_mood(('bored', 3000, 100))
#write_tabel_mood(('dirty', 1000, 100))
#write_tabel_mood(('ill', 5000, 100))

def alter_tabel_mood(data_name,data_content):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE mood SET {}={};".format(data_name, data_content) # image_path CHAR(200)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_mood: ERROR: ', msg)
    except Exception as msg:
        logging.debug('alter_tabel_mood: ERROR:', msg)
    finally:
        if con:
            con.close()

def alter_tabel_mood_where(data_name, data_content, where, what):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE mood SET {}='{}' WHERE {}='{}';".format(data_name, data_content, where, what)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print(command)
        print('alter_tabel_mood_where: ERROR: ', msg)
    finally:
        if con:
            con.close()

#alter_tabel_mood_where('name', 'hungry', 'id', 1)

def read_everything_from_tabel_mood():
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT * FROM mood"
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        logging.debug("read_everything_from_tabel_mood: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_everything_from_tabel_mood: ERROR:', msg)
    finally:
        if con:
            con.close()
#moods = read_everything_from_tabel_mood()
#print(moods)

def read_value_from_tabel_mood(value, where, what):
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT {} FROM mood WHERE {}={};".format(value, where, what)
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        return data
    except Exception as msg:
        print(msg)
        #logging.debug('read_value_from_tabel_mood: ERROR:', msg)
    finally:
        if con:
            con.close()

