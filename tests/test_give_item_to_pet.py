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


def give_item_to_pet(item):
    data_effect = read_value_from_tabel_mood_changing_item('effect', 'item', item )
    effect = data_effect[0][0]
    print(effect)
    data_mood = read_value_from_tabel_mood_changing_item('mood', 'item', item )
    effect_on = data_mood[0][0]
    print(effect_on)
    mood_data = read_everything_from_tabel_mood()
    for element in mood_data:
        id_num, name, max_value, current_value = element 
        if name==effect_on and current_value < max_value:
            current_value += effect
            if current_value > max_value:
                current_value = max_value
            alter_tabel_mood_where('current_value', current_value, 'id', id_num)

give_item_to_pet('Berry')
    
