# -*- coding: utf-8 -*-
import logging
# for DB usage
import sqlite3


logging.basicConfig(filename='log.txt',level=logging.DEBUG) 

#Voc
def make_tabel_voc():
    try:
        con = sqlite3.connect('game.db')
        con.execute('''CREATE TABLE IF NOT EXISTS voc (
            id INTEGER PRIMARY KEY, 
            question CHAR(100) NOT NULL, 
            answer CHAR(100) NOT NULL, 
            times_answered_correctly INT,
            question_language CHAR(100),
            answer_language CHAR(100)          
            )
            ''') 
        #  due_on FLOAT
        #  due BOOL
        con.commit()
        con.close()
    except Exception as msg:
        logging.debug('make_tabel_voc: ERROR: ', msg)
        print(msg)

#make_tabel_voc()

def write_tabel_voc(data):
    question, answer, times_answered_correctly, question_language, answer_language = data
    try: 
        con = sqlite3.connect('game.db')
        con.execute('INSERT INTO voc (question, answer, times_answered_correctly, question_language, answer_language) VALUES (?,?,?,?,?);',(question, answer, times_answered_correctly, question_language, answer_language))
        con.commit()
    except Exception as msg:
        logging.debug('write_tabel_voc: Error', msg)
    finally:
        if con:
            con.close()

#write_tabel_voc(('Hello','Hallo',0, 'german'))
#write_tabel_voc(('Guten Abend','Good evening',0,'german'))
#write_tabel_voc(('Wo ist ...?','Where is ...?',0,'german'))
#write_tabel_voc(('Ich bin ...','I am ...',0, 'german'))
#write_tabel_voc(('Ich habe Hunger.','I am hungry.',0, 'german'))
#write_tabel_voc(('Help!','Hilfe!',0, 'german'))
#write_tabel_voc(('Bye!','Tschüss!',0, 'german'))

def alter_tabel_voc(data_name,data_content):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE voc SET {}={};".format(data_name, data_content) # image_path CHAR(200)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_voc: ERROR: ', msg)
        logging.debug('alter_tabel_voc: ERROR:', msg)
    finally:
        if con:
            con.close()
#alter_tabel_voc('times_answered_correctly', 3)

def alter_tabel_voc_where(data_name, data_content, where, what):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE voc SET {}='{}' WHERE {}={};".format(data_name, data_content, where, what) # image_path CHAR(200)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_voc: ERROR: ', msg)
        logging.debug('alter_tabel_voc: ERROR:', msg)
    finally:
        if con:
            con.close()
#alter_tabel_voc_where('times_answered_correctly', 5, 'id', 2)

def read_everything_from_tabel_voc():
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT * FROM voc"
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        #logging.debug("read_everything_from_tabel_voc: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_everything_from_tabel_voc: ERROR:', msg)
    finally:
        if con:
            con.close()
#data = read_everything_from_tabel_voc()
#print(data)

def read_value_from_tabel_voc(value, where, what):
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT {} FROM voc WHERE {}={}".format(value, where, what)
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        #logging.debug("read_value_from_tabel_voc: {}".format(data))
        #print(data)
        return data
    except Exception as msg:
        logging.debug('read_value_from_tabel_voc: ERROR:', msg)
    finally:
        if con:
            con.close()
