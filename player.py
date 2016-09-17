# -*- coding: utf-8 -*-
import logging
# for DB usage
import sqlite3

logging.basicConfig(filename='log.txt',level=logging.DEBUG)

#Player
def make_tabel_player(): 
    try:
        con = sqlite3.connect('game.db')
        con.execute('''CREATE TABLE IF NOT EXISTS player (
            id INTEGER PRIMARY KEY, 
            name CHAR(100) NOT NULL,
            score INT, 
            id_of_last_question_asked INT,
            combo INT)
            ''') 
        con.commit()
        con.close()
    except Exception as msg:
        print('make_tabel_player: ERROR: ', msg)

#make_tabel_player()

def write_tabel_player(data):
    name, score = data
    try:
        con = sqlite3.connect('game.db')
        con.execute("INSERT INTO player (name, score) VALUES (?, ?, ?);",(name, score)) #add other
        con.commit()
        con.close()
        #logging.debug("write_tabel_player: wrote data: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('write_tabel_player: ERROR:', msg)
    finally:
        if con:
            con.close()   

#write_tabel_player(('marionline', 0))

def alter_tabel_player(data_name, data_content):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE player SET {}='{}';".format(data_name, data_content) # image_path CHAR(200)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_player_where: ERROR:', msg)
        print(command)
        #logging.debug('alter_tabel_player: ERROR:', msg)
    finally:
        if con:
            con.close()

def alter_tabel_player_where(data_name, data_content, where, what):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE player SET {}='{}' WHERE {}={} ;".format(data_name, data_content, where, what) # image_path CHAR(200)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_player_where: ERROR:', msg)
        print(command)
    finally:
        if con:
            con.close()

#alter_tabel_player('score', 5)

def read_everything_from_player_table():
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT * FROM player"
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        #logging.debug("read_everything_from_player_table: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_everything_from_player_table: ERROR:', msg)
    finally:
        if con:
            con.close()

def read_last_question_from_player_table():
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT id_of_last_question_asked FROM player" # WHERE id=player_id <- if we had several players 
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        return data
    except Exception as msg:
        logging.debug('read_everything_from_player_table: ERROR:', msg)
    finally:
        if con:
            con.close()

def read_value_from_whole_player_tabel(value):
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT {} FROM player".format(value)
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        return data
    except Exception as msg:
        logging.debug('read_value_from_player_tabel: ERROR:', msg)
    finally:
        if con:
            con.close()
