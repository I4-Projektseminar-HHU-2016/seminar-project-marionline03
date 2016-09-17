 #import datetime
import logging

# for DB usage
import sqlite3

#for pet creation
import random

# Pet 
def make_tabel_pet(): 
    try:
        con = sqlite3.connect('game.db')
        con.execute('''CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY, 
            name CHAR(100) NOT NULL, 
            life_points INT, 
            current_life_points INT,
            current_state INT,
            body_img CHAR(150),
            face_img CHAR(150),
            deco_img CHAR(150)
            )
            ''') 
        con.commit()
        con.close()
    except Exception as msg:
        print('make_tabel_pet: ERROR: ', msg)

#make_tabel_pet()

def write_into_tabel_pet(data):
    # add other
    name, life_points, current_life_points, current_state, body, face, deco = data
    try:
        con = sqlite3.connect('game.db')
        con.execute("INSERT INTO pet (name, life_points, current_life_points, current_state, body_img, face_img, deco_img) VALUES (?, ?, ?, ?, ?, ?, ?);",(name, life_points,  current_life_points, current_state, body, face, deco)) #add other
        con.commit()
        con.close()
        logging.debug("write_tabel_pet: wrote data: {}".format(data))
        return data
    except Exception as msg:
        print(msg)
        logging.debug('write_tabel_pet: ERROR:', msg)
    finally:
        if con:
            con.close()

# make pet
#face= random.choice(['neutral01.png', 'neutral02.png', 'happy01.png', 'happy02.png'])
#body= random.choice(['red.png', 'violet.png', 'blue.png','green.png','turquoise.png','yellow.png'])
#deco= random.choice(['alien.png','antenna.png', 'triangle.png', 'tiger.png','rabbit.png','spots.png'])
#write_into_tabel_pet(('Alien', 100, 100, 2, body, face, deco))

def alter_tabel_pet(data_name, data_content):
    try:
        con = sqlite3.connect('game.db')
        command="UPDATE pet SET {}='{}';".format(data_name, data_content) # image_path CHAR(200)
        con.execute(command) 
        con.commit()
        con.close()
    except Exception as msg:
        print('alter_tabel_pet: ERROR: ', msg)
    except Exception as msg:
        logging.debug('alter_tabel_pet: ERROR:', msg)
    finally:
        if con:
            con.close()

alter_tabel_pet('current_state', 2)

def read_everything_from_tabel_pet():
    try:
        con = sqlite3.connect('game.db')
        command ="SELECT * FROM pet"
        c = con.cursor()  
        c.execute(command)
        data = c.fetchall()
        logging.debug("read_everything_from_tabel_pet: {}".format(data))
        return data
    except Exception as msg:
        logging.debug('read_everything_from_tabel_pet: ERROR:', msg)
    finally:
        if con:
            con.close()
            
#read_everything_from_tabel_pet()
