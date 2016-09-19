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

logging.basicConfig(filename='log.txt',level=logging.DEBUG)

#TODO: export voc s json
'''def make_json_vocabulary_data():
    data = read_everything_from_tabel_voc()
    # http://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    # sort by 3rd value (score), low score comes first    
    output = sorted(data, key=itemgetter(3))
    my_dict={}
    for element in output:
        if element[3] in my_dict.keys():
            my_dict[element[3]].append(element)
        else:
            my_dict[element[3]] = []
            my_dict[element[3]].append(element)
    output=josm.dumps(my_dict)
    return output
 
# make_json_vocabulary_data()'''

NAV = [("Pet's home", '/play'),('Word-List', '/wordlist'),('Practice', '/learn'), ('Shopping', '/shop'),('Pet', '/pet'),('Player', '/player')]
FOOTER = 'vocabulary pet game written in python -- vocabulary pet (Title), marionline(Author), github-repository(Source), ?(License)'
#Font familiy:  Helvetica <- unix

@route('/pet_image')
def set_pet_image(data_list):
    return random.choice(['neutral01.png', 'neutral02.png', 'happy01.png', 'happy02.png'])    

@route('/test')
def test():
    print('test')
    return template('test')

def set_pet_images(mood):
    if mood == 'normal':
        happy_faces =['neutral01.png', 'neutral02.png', 'happy01.png', 'happy02.png']
        face = random.choice(happy_faces)
        speechbubble=''
    if mood=='hungry':
        unhappy_faces =['angry01.png', 'angry02.png', 'outch01.png', 'outch02.png']
        face = random.choice(unhappy_faces)
        speechbubble=random.choice(['want_food.png','think_of_eating00.png'])
    return (face, speechbubble)

@route('/update')
def update():
    pet_data = read_everything_from_tabel_pet()
    id_num, name, life_points, current_life_points, current_state, body, face, deco = pet_data[0]
    current_mood_data = read_value_from_tabel_mood('name', 'id', current_state)
    current_mood = current_mood_data[0][0]
    mood_data = read_everything_from_tabel_mood()
    for element in mood_data:
        mood_id_num, mood_name, mood_max_value, mood_value = element
        if mood_name != current_mood:
            if mood_name == 'normal':
                pass
            elif mood_value > 0:
                result = mood_value -1
                alter_tabel_mood_where('current_value', result, 'name', element[1])
            elif mood_value == 0:
                alter_tabel_pet('current_state', mood_id_num)
    
    pet_data = read_everything_from_tabel_pet()
    id_num, name, life_points, current_life_points, current_state, body, face, deco = pet_data[0]
    mood_data = read_value_from_tabel_mood('name', 'id', current_state)
    mood = mood_data[0][0]
    face, speechbubble = set_pet_images(mood)
    output = {'face':face, 'body':body, 'deco':deco, 'speechbubble':speechbubble}
    return json.dumps(output)


def give_item_to_pet(item):
    data_effect = read_value_from_tabel_mood_changing_item('effect', 'item', item)
    effect = data_effect[0][0]
    data_mood = read_value_from_tabel_mood_changing_item('mood', 'item', item)
    effect_on = data_mood[0][0]
    print('The item effects {}, with a value of {}'.format(effect_on, effect))
    mood_data = read_everything_from_tabel_mood()
    for element in mood_data:
        id_num, name, max_value, current_value = element
        if name == effect_on and current_value < max_value:
            current_value += effect
            alter_tabel_pet('current_state', 2) # 2 is normal mood
            if current_value > max_value:
                current_value = max_value
            alter_tabel_mood_where('current_value', current_value, 'id', id_num)
    
@route('/json_player_data')
def send_player_json():
    data_dict = make_json_vocabulary_data()
    return json.dumps(data_dict)
    
#TODO: static_path
@route('/<filename>')
def server_static(filename):
    return static_file(filename, root=STATIC_PATH) #<- change this path according to your directory!     

@route('/player')
def player():
    data = read_everything_from_player_table()
    id_num, name, score, id_of_last_question, combo = data[0]
#TODO: Optional add more info: statistics on VOC (per matplotlib data) + Badges
    return template('player', menu=NAV, footer=FOOTER, data=[id_num, name, score, combo])

@route('/pet')
def pet():
    data = read_everything_from_tabel_pet()
    id_num, name, life_points, current_life_points, current_state, body, face, deco= data[0]
    mood_data = read_value_from_tabel_mood('name', 'id', current_state)
    mood = mood_data[0][0]
#TODO: Optional add more info: Age, Birthday, Favorite Food/Item/Voc
    face, speechbubble = set_pet_images(mood)
    alter_tabel_pet('face', face)
    return template('pet', menu=NAV, footer=FOOTER, data=[id_num, name, life_points, mood], body=body, face=face, deco=deco, speechbubble=speechbubble,)

@route('/wordlist')
def wordlist():
    data = read_everything_from_tabel_voc()
    return template('wordlist', menu=NAV, footer=FOOTER, data=data)

@post('/wordlist')
def edit_wordlist():
    id_num = request.forms.get('id')
    question = request.forms.get('question')
    answer = request.forms.get('answer')
    question_language = request.forms.get('question_language')
    answer_language = request.forms.get('answer_language')
    alter_tabel_voc_where('question', question, 'id',id_num)
    alter_tabel_voc_where('answer', answer, 'id',id_num)
    alter_tabel_voc_where('question_language', question_language, 'id',id_num)
    alter_tabel_voc_where('answer_language', answer_language, 'id',id_num)
    data = read_everything_from_tabel_voc()
    return template('wordlist', menu=NAV, footer=FOOTER, data=data)

@route('/learn')
def learn():
    data = read_everything_from_tabel_voc()
    # http://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    # sort by 3rd value (score), low score comes first    
    output = sorted(data, key=itemgetter(3))
    my_dict={}
    for element in output:
        if element[3] in my_dict.keys():
            my_dict[element[3]].append(element)
        else:
            my_dict[element[3]] = []
            my_dict[element[3]].append(element)
    keys = sorted(list(my_dict.keys()))
    output= random.choice(my_dict[keys[0]])
    alter_tabel_player('id_of_last_question_asked', output[0])
    pet_data = read_everything_from_tabel_pet()
    pet_id_num, pet_name, pet_life_points, pet_current_life_points, pet_current_state, pet_body, pet_face, pet_deco = pet_data[0]
    return template('learn', msg='', question=output, menu=NAV, footer=FOOTER, body=pet_body, face=pet_face, deco=pet_deco) 

@route('/learn', method='POST')
def learn_check_answer():
    player_data_list = read_everything_from_player_table()
    player_id_num, player_name, score, id_of_last_question_asked, combo = player_data_list[0]
    answer = request.forms.get('answer')
    voc_list = read_value_from_tabel_voc('*', 'id' , id_of_last_question_asked)
    voc_id_num, question, expected_answer, times_answered_corectly, question_language, answer_language = voc_list[0]
    # tricky:  http://stackoverflow.com/questions/27432211/python-bottle-requests-and-unicode <- ignoriert
    answer = answer.replace("Ã¤",'ö').replace("Ã¶","ä").replace("Ã¼","ü")
    msg=''
    points = 0
    pet_data = read_everything_from_tabel_pet()
    pet_id_num, pet_name, pet_life_points, pet_current_life_points, pet_current_state, pet_body, pet_face, pet_deco = pet_data[0]
    if combo == None:
        combo = 0
    if times_answered_corectly == None:
        times_answered_corectly =0
    if answer.lower() == expected_answer.lower():
        times_answered_corectly +=1
        happy_faces =['happy01.png', 'happy02.png']
        face = random.choice(happy_faces)
        if combo > 100:
            combo = 0
            points = 200
            combo += 1
            msg = ["Unbelivable!", "You answered correctly 100 times in a row.", "That's astonishing! You reward are 200 points."]
        elif combo == 50:
            points = 50
            combo += 1
            msg=["I am speechless!", "You answered correctly 50 times in a row.", "That means 50 extra points for you."]
        elif combo == 40:
            points = 40
            combo += 1
            msg=["Excellent!","40 times in a row and no mistake!","You earned yourself 40 extra points."]
        elif combo == 30:
            points = 30
            combo += 1
            msg=["Chapeau!", "In the last 30 answers you made no mistake.", "Your reward is a bomus of 30 points."]
        elif combo == 20:
            points = 20
            combo += 1
            msg=["Very good!", "You know what you are doing.", "For 20 correct answers in a row, you get an extra point bonus."]
        elif combo == 15:
            points = 15
            combo += 1
            msg=["15 times in a row.", "+15 Points.", "You are getting better."]
        elif combo == 10:
            points = 10
            combo += 1
            msg=["Did you see that?","You aswered correctly 10 times in a row.", "You get 10 extra points. Keep going!"]
        else:
            points += 1
            combo += 1
            score += points
            msg=['Your score is: {}'.format(score)]
        score += points
    else:
        combo = 0    
        points = 0
        msg=['The question was: {}'.format(question), 'The target language was {}.'.format(answer_language),'The correct answer is: {}'.format(expected_answer),'You said: {}'.format(answer)] 
        unhappy_faces =['angry01.png', 'angry02.png', 'outch01.png', 'outch02.png', 'neutral01.png', 'neutral02.png']
        face = random.choice(unhappy_faces)
    alter_tabel_player_where('score', score, 'id', player_id_num)
    alter_tabel_player_where('combo', combo, 'id', player_id_num)
    alter_tabel_voc_where(' times_answered_correctly',times_answered_corectly,'id', voc_id_num)
    data = read_everything_from_tabel_voc()
    sorted_data = sorted(data, key=itemgetter(3))
    my_dict={}
    for element in sorted_data:
        if element[3] in my_dict.keys():
            my_dict[element[3]].append(element)
        else:
            my_dict[element[3]] = []
            my_dict[element[3]].append(element)
    keys = sorted(list(my_dict.keys()))
    output= random.choice(my_dict[keys[0]])
    #print('output: ', output[0])
    alter_tabel_player('id_of_last_question_asked', output[0])
    return template('learn', msg=msg, question=output, menu=NAV, footer=FOOTER, face=face, body=pet_body, deco=pet_deco) 

@route('/shop')
def shop():
    data = read_everything_from_tabel_item()
    score_data =read_value_from_whole_player_tabel('score')
    money = score_data[0][0] 
    data = read_everything_from_tabel_item()
    return template('shop', data=data, money=money, menu=NAV, footer=FOOTER) 


@post('/shop')
def buy():
    id_num = request.forms.get('id')
    print(id_num)
    item_data = read_value_from_tabel_item('*', 'id', id_num)
    print(item_data)
    id_num_item, item_name, description, image, price = item_data[0]
    player_id = read_value_from_whole_player_tabel('id') #nur bei 1 Player in DB, sonst id des spielers erfragen z.B. durch cookie 
    player_score = read_value_from_whole_player_tabel('score') 
    if player_score[0][0] >= price:
        result = player_score[0][0] - price
        alter_tabel_player_where('score', result, 'id', player_id[0][0])
        #print('item_name', item_name)
        amount_data = read_value_from_tabel_inventory('amount', 'item_name', item_name)
        #print('amount_data', amount_data)
        if amount_data == None or amount_data == []:
            #print('writing tabel row: {}'.format(item_name))
            write_tabel_inventory((item_name, 1))
        else:
            amount = amount_data[0][0]
            #print('amount', amount)
            amount += 1
            #print('You have {} {}s.'.format(amount, item_name))
            alter_tabel_inventory_where('amount', amount, 'item_name', item_name)
    score_data =read_value_from_whole_player_tabel('score')
    money = score_data[0][0] 
    data = read_everything_from_tabel_item()
    return template('shop', data=data, money=money, menu=NAV, footer=FOOTER) 


@route('/')
@route('/index')
@route('/play')
def play():
    inventory_data=read_everything_from_table_inventory()
    inventory_list = []
    inventory_empty = True
    for element in inventory_data:
        id_num, name, amount = element
        item_data = read_value_from_tabel_item('*', 'name', name)
        id_num_item, item_name, description, image, price = item_data[0]
        inventory_list.append((id_num_item, name, description, image, amount))
        if 0 < amount:
            inventory_empty = False
    pet_data = read_everything_from_tabel_pet()
    id_num, name, life_points, current_life_points, current_state, body, face, deco = pet_data[0]
    mood_data = read_value_from_tabel_mood('name', 'id', current_state)
    mood = mood_data[0][0]
    face, speechbubble =  set_pet_images(mood)
    return template('play', menu=NAV, footer=FOOTER, inventory=inventory_list, face=face, body=body, deco=deco, speechbubble=speechbubble,inventory_empty=inventory_empty) 


@route('/play', method='POST')
def post_play():
    inventory_data=read_everything_from_table_inventory()
    inventory_list = []
    for element in inventory_data:
        id_num, name, amount = element
        item_data = read_value_from_tabel_item('*', 'name', name)
        id_num_item, item_name, description, image, price = item_data[0]
        inventory_list.append((id_num_item, name, description, image, amount))
    id_num_item_clicked = request.forms.get('id')
    if not id_num_item_clicked == None:
        print('id_num_item_clicked: ',id_num_item_clicked)
        item_data_item_clicked = read_value_from_tabel_item('*', 'id', id_num_item_clicked)
        print('item_data_item_clicked', item_data_item_clicked)
        id_num_item_clicked, name_item_clicked, description_item_clicked, image_item_clicked, price_item_clicked = item_data_item_clicked[0]
        print('name_item_clicked', name_item_clicked)
        amount_data = read_value_from_tabel_inventory('amount', 'item_name', name_item_clicked)
        print('amount_data', amount_data)
        amount = amount_data[0][0]
        amount -= 1
        alter_tabel_inventory_where('amount', amount, 'item_name', name_item_clicked)  
    give_item_to_pet(name)
    #reload
    inventory_data=read_everything_from_table_inventory()
    inventory_list = []
    inventory_empty=True
    for element in inventory_data:
        id_num, name, amount = element
        item_data = read_value_from_tabel_item('*', 'name', name)
        id_num_item, item_name, description, image, price = item_data[0]
        inventory_list.append((id_num_item, name, description, image, amount))
        if 0 < amount:
            inventory_empty = False
    pet_data = read_everything_from_tabel_pet()
    id_num, name, life_points, current_life_points, current_state, body, face, deco = pet_data[0]
    mood_data = read_value_from_tabel_mood('name', 'id', current_state)
    mood = mood_data[0][0]
    face, speechbubble = set_pet_images(mood)    
    return template('play', menu=NAV, footer=FOOTER, inventory=inventory_list, face=face, body=body, deco=deco, speechbubble=speechbubble, inventory_empty=inventory_empty)
  
run(host=HOST, port=PORT, debug=True, reloader=True)
