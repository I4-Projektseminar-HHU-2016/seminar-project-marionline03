# -*- coding: utf-8 -*-
from bottle import route, run, template, get, post, request, response, error, static_file, redirect
from hidden_server_data import PORT, HOST, STATIC_PATH
from voc import read_everything_from_tabel_voc, alter_tabel_voc_where, read_value_from_tabel_voc
from player import read_last_question_from_player_table, read_everything_from_player_table, alter_tabel_player, alter_tabel_player_where, read_value_from_whole_player_tabel
from pet import read_everything_from_tabel_pet, alter_tabel_pet
from item import read_value_from_tabel_item, read_everything_from_tabel_item
from mood import read_everything_from_tabel_mood, read_value_from_tabel_mood, alter_tabel_mood_where
from mood_changing_items import read_value_from_tabel_mood_changing_item
from inventory import read_value_from_tabel_inventory, write_tabel_inventory, alter_tabel_inventory_where, read_everything_from_table_inventory
#delete_amount_zero_rows_from_tabel 
from operator import itemgetter 
import random
import logging
import json

@route('/update')
def update():
    pet_data = read_everything_from_tabel_pet()
    id_num, name, life_points, current_life_points, current_state, body, face, deco = pet_data[0]
    current_mood_data = read_value_from_tabel_mood('name', 'id', current_state)
    current_mood = current_mood_data[0][0]
    print('current_mood:', current_mood) 
    mood_data = read_everything_from_tabel_mood()
    for element in mood_data:
        print(element)
        mood_id_num, mood_name, mood_max_value, mood_value = element
        if mood_name != 'normal' or mood_name != current_mood:
            if mood_value > 0:
                result = mood_value -1
                print(result)
                alter_tabel_mood_where('current_value', result, 'name', element[1])
            elif mood_value == 0:
                print("set mood to {} with id {}".format(mood_name, mood_id_num))
                alter_tabel_pet('current_state', mood_id_num)
    
    pet_data = read_everything_from_tabel_pet()
    id_num, name, life_points, current_life_points, current_state, body, face, deco = pet_data[0]
    mood_data = read_value_from_tabel_mood('name', 'id', current_state)
    mood = mood_data[0][0]
    if mood == 'normal':
        happy_faces =['neutral01.png', 'neutral02.png', 'happy01.png', 'happy02.png']
        face = random.choice(happy_faces)
    else:
        unhappy_faces =['angry01.png', 'angry02.png', 'outch01.png', 'outch02.png']
        face = random.choice(unhappy_faces)
    alter_tabel_pet('face_img', face)
    output = {'face':face, 'body':body, 'deco':deco}
    return json.dumps(output)

update()
