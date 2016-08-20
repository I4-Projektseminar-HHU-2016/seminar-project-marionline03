# Sources used:  
# Bottle Doku: bottlepy.org/docs/dev/index.thml

import random
import bottle
from bottle import route, run, template, static_file, request, redirect
from do_not_upload import STATIC_FILES_PATH
from read_write_csv import Datamanager
from pet import Pet
from player import Player
from badge import Badge, welcome_badge, gave_10_berries_to_pet
import time
from voc import Voc
from food import berry, raspberry

INTERVAL = 700  # how fast the page reloads - in miliseconds  

# reload part of webpage:
# -> stackoerflow: http://stackoverflow.com/questions/12399952/only-reload-a-part-of-a-web-page

datamanager = Datamanager()

def sort_vocabulary_by_due_time(vocs):
    duelist = [] # these vocs will be asked
    waitlist = [] # are not to be asked now, asked later
    
    # Todo: how to filter these? by due_time = 0?
    unseen_list = [] # where never asked before, new/unseen
    
    for voc in vocs:
        # not due 
        while time.time() <= voc.due_time:
            # how long to wait till word needs to be asked again?
            time_to_wait = voc .due_time- time.time()
            voc.is_due_in = time_to_wait
        # due
        else:
            duelist.append(voc)
    return (duelist, waitlist)


def update(pet, player):
    # after the data is loaded, 
    # update calls the classes update-functions
    pet.change_status()
    
    #TODO: where,+ when update vocabulary?
    # wohin wird das returnt? Wer fragt das an?
    #sort_vocabulary_by_due_time()
    pass


@route('/inventory')
def show_inventory():
    #player.get_inventory()
    pass
    
# if user clicks something
@route('/inventory', method='POST')
def handle_inventory_event():
    # TODO
    # get from input
    pass
    # what form input? use, delete? 
    
    # on item use 
        #return #gamescreen #with eating monster animation
    # on item deletion  
        #return #inventory
       
@route('/wordlist')
def show_wordlist():
    #TODO
    # request voc data
    
    # make displayable of voc data
    return template('table goes here')

@route('/<filename>')
def serve_static(filename):
    return static_file(filename, root=STATIC_FILES_PATH)

#@route('<filename>')
#def give_static(filename):
#    return static_file(filename, root='/static/')


@route('/feed_item', method='POST')
def feed_item():
    # load data
    player_data = datamanager.read_json_data('player.json')
    pet_data = datamanager.read_json_data('pet.json')
    
    #create objects 
    pet = Pet(pet_data['name'], pet_data['hp'], pet_data['status'], pet_data['image'], pet_data['imagelist'], pet_data['level'], pet_data['exp'])
    
    #create badges that player still can arcieve they are imported from badges.py, but could be created here as well, 
    #TODO create badges here means to import their data from player.json or somewhere else!
    possible_badge_list = []
    for badge in player_data['badges']:
        if badge == 'welcome_badge':
            possible_badge_list.append(welcome_badge)
        elif badge == 'gave_10_berries_to_pet':    
            possible_badge_list.abbend(gave_10_berries_to_pet)
    
    #create items to be put in player's inventory 
    
    #finally create the player class 
    player = Player(player_data['name'], player_data['image'], player_data['score'], possible_badge_list)
     
    # load item data
    player_choice = request.forms.get('food')
    print('Player choose to give a {} to the pet.'.format(player_choice))
    
    # check for all actions that are possible
    for badge in player.possible_badges:
        if 'feed_item' in badge.action:
            badge.on_player_action()
        else:
            pass
    
    # make food item:
    if player_choice == 'berry':
        pet.receive_food(berry)
    elif player_choice == 'raspberry':
        pet.receive_food(raspberry)    
    
    # add a message like 'pet ate food'?
    redirect('/')
    

@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


@route('/')
def show_index():
    # everything should be re-routed to hello when there is no data set
    #TODO: handle Exception if file not found
    player_data = datamanager.read_json_data('player.json')
    pet_data = datamanager.read_json_data('pet.json')
    voc_data = datamanager.read_csv_data('voc.csv')
    #create objects 
    pet = Pet(pet_data['name'], pet_data['hp'], pet_data['status'], pet_data['image'], pet_data['imagelist'], pet_data['level'], pet_data['exp'])
    player = Player(player_data['name'], player_data['image'], player_data['score'], player_data['badges'])
    vocs = []
    for element in voc_data:
        question =element[0]
        meaning = element[1]
        hint = element[2]
        lesson = element[3]
        language = element[4]
        answered_corrcetly_counter = int(element[5])
        answered_counter = int(element[6])
        time_last_answered = float(element[7])
        due_time = float(element[8])
        vocs.append(Voc(question, meaning, hint, lesson, language, answered_corrcetly_counter, answered_counter, time_last_answered, due_time))
        
    # sort vocs
    duelist, waitlist = sort_vocabulary_by_due_time(vocs)
    print('duelist: ', duelist)
    print('waitlist: ', waitlist)
    #update
    update(pet, player)
        
    # set images etc.
    pet_image = set_pet_image(pet.image_list)
    
    # export
    known_states = []
    for element in pet.known_states.keys():
        status_dict = {"name":pet.known_states[element].value, "value":pet.known_states[element].value, "image_list":pet.known_states[element].image_list}
        known_states.append(status_dict) 
    
    # write pet data
    pet_dict = {"name": pet.name, "hp":pet.hp, "known_states":known_states, "status": pet.status.name, "hungry_in": pet.status.value, "image": pet.image, "imagelist":pet.image_list, "level": pet.level, "exp":pet.exp} 
    datamanager.write_json_data('pet.json', pet_dict)
    
    # write player data
    #TODO
    player_dict={}
    
    # write voc_data 
    # but this hasen't been changed! -> no need to export this
    # export needs only be used in word edit mode or learning mode!
    #TODO: voc_data has to be dictionary!
    #datamanager.write_csv_data('voc.csv', voc_data)
    
    # make displayable content
    menu_content = [('Learn','/learningmode', 'button_learn.png'),('items','/inventory', 'button_inventory.png'),('Buy','/buy', 'button_buy.png'),('words', '/wordlist', 'button_words.png'),('Player','/settings', 'button_settings.png')]
   
    # change show_badges to either show bades in progress, and if there are none, show what badges could be progressed
    if player.progressing_badges == []:
        show_badges = player.possible_badges
    else:
        show_badges = player.progressing_badges    
    
    return template('page', interval=INTERVAL, menu=menu_content, pet_image=pet_image,  due_list=duelist, wait_list=waitlist, badges=show_badges, pet_status=pet.status.name, pet_hunger=pet.known_states['hungry'].value)

@route('/pet_image')
def set_pet_image(data_list):
    return random.choice(data_list)    
    
    
@route('/learningmode')
def choose_mode():
    # read data
    player_data = datamanager.read_json_data('player.json')
    pet_data = datamanager.read_json_data('pet.json')
    #create objects 
    
    # TODO: pet's hungry_value needs to be saved and imported!
    pet = Pet(pet_data['name'], pet_data['hp'], pet_data['status'], pet_data['image'], pet_data['imagelist'], pet_data['level'], pet_data['exp'])
    player = Player(player_data['name'], player_data['image'], player_data['score'], player_data['badges'])
    
    # make displayable content
    menu_content = [('Learn','learningmode', 'button_learn.png'),('items','/inventory', 'button_inventory.png'),('Buy','/buy', 'button_buy.png'),('words', '/wordlist', 'button_words.png'),('Player','/settings', 'button_settings.png')]
    # change show_badges to either show bades in progress, and if there are none, show what badges could be progressed
    if player.progressing_badges == []:
        show_badges = player.possible_badges
    else:
        show_badges = player.progressing_badges
    # return template + variables   
    
    #reset combo
    try:
        combo = datamanager.read_file('combo.txt') # if there is no combo      
    except:
        combo = 0
    if not combo == 0:
        combo = 0
        datamanager.write_file('combo.txt', str(combo))   
    return template('choose_learn_method', interval=INTERVAL, menu=menu_content, badges=show_badges, learning_mode=[('write','writing test'),('mulpile choice', 'multiple_choice'), ('flash card mode','flash_card'), ('memory game', 'memory')] )
      
@route('/write')
def writing_test():
    # import voc data, active question, expected answer
    #TODO: handle Exception if file not found
    player_data = datamanager.read_json_data('player.json')
    pet_data = datamanager.read_json_data('pet.json')
    voc_data = datamanager.read_csv_data('voc.csv')
        
    #create objects 
    pet = Pet(pet_data['name'], pet_data['hp'], pet_data['status'], pet_data['image'], pet_data['imagelist'], pet_data['level'], pet_data['exp'])
    player = Player(player_data['name'], player_data['image'], player_data['score'], player_data['badges'])
    vocs = []
    for element in voc_data:
        question =element[0]
        meaning = element[1]
        hint = element[2]
        lesson = element[3]
        language = element[4]
        answered_corrcetly_counter = int(element[5])
        answered_counter = int(element[6])
        time_last_answered = float(element[7])
        due_time = float(element[8])
        vocs.append(Voc(question, meaning, hint, lesson, language, answered_corrcetly_counter, answered_counter, time_last_answered, due_time))
        
    # sort vocs
    duelist, waitlist = sort_vocabulary_by_due_time(vocs)
    print('duelist: ', duelist)
    print('waitlist: ', waitlist)
    #update
    update(pet, player)
    player = Player(player_data['name'], player_data['image'], player_data['score'], player_data['badges'])
    
    ask_for_voc = random.choice(duelist)
    print (ask_for_voc)
    print(ask_for_voc.question)
    print(ask_for_voc.meaning)
    # save question, answer in text file for persistence
    # TODO: hash answer , write hash
    datamanager.write_file('answer.txt', ask_for_voc.meaning)
    datamanager.write_file('question.txt', ask_for_voc.question)
    
    # display
    # make displayable content
    menu_content = [('Learn','learningmode', 'button_learn.png'),('items','/inventory', 'button_inventory.png'),('Buy','/buy', 'button_buy.png'),('words', '/wordlist', 'button_words.png'),('Player','/settings', 'button_settings.png')]
    # change show_badges to either show bades in progress, and if there are none, show what badges could be progressed
    if player.progressing_badges == []:
        show_badges = player.possible_badges
    else:
        show_badges = player.progressing_badges
    
    return template('writing', menu=menu_content, badges=show_badges, voc=ask_for_voc, vocs_due=len(duelist), vocs_wait=len(waitlist), vocs_all=len(duelist)+len(waitlist))


@route('/write', method='POST')
def writing_mode():
    # import voc data, active question, expected answer
    # import voc data, active question, expected answer
    #TODO: handle Exception if file not found
    player_data = datamanager.read_json_data('player.json')
    pet_data = datamanager.read_json_data('pet.json')
    voc_data = datamanager.read_csv_data('voc.csv')
    
    #read data
    #TODO: read hashed_answer
    try:
        answer = datamanager.read_file('answer.txt')
        question =datamanager.read_file('question.txt')
        combo = datamanager.read_file('combo.txt')
        
    except Exception as msg:
        print("Error: {}".format(msg))
        combo == '0'
    #get input
    user_input = request.forms.get('answer')
        
    #create objects 
    pet = Pet(pet_data['name'], pet_data['hp'], pet_data['status'], pet_data['image'], pet_data['imagelist'], pet_data['level'], pet_data['exp'])
    player = Player(player_data['name'], player_data['image'], player_data['score'], player_data['badges'])
    vocs = []
    for element in voc_data:
        question =element[0]
        meaning = element[1]
        hint = element[2]
        lesson = element[3]
        language = element[4]
        answered_corrcetly_counter = int(element[5])
        answered_counter = int(element[6])
        time_last_answered = float(element[7])
        due_time = float(element[8])
        vocs.append(Voc(question, meaning, hint, lesson, language, answered_corrcetly_counter, answered_counter, time_last_answered, due_time))
        
    # sort vocs
    duelist, waitlist = sort_vocabulary_by_due_time(vocs)
    print('duelist: ', duelist)
    print('waitlist: ', waitlist)
    
    # analyze result
    print(answer)
    print(type(answer))
    print(user_input)
    print(type(user_input))
    result = False
    combo = int(combo)
    if answer == user_input:
        result = True
        combo +=1
        if combo == 100:
            combo = 0
            points = 200
        elif combo == 50:
            points = 100
        elif combo == 40:
            points = 40
        elif combo == 30:
            points = 30
        elif combo == 20:
            points = 20
        elif combo == 15:
            points = 15
        elif combo == 10:
            points = 10
        else:
            points = 1
        player.increase_scrore(points)
        #TODO: 
        #give player points
        # display a gratulation image: happy pet
    else:
        combo = 0    
        points = 0
    datamanager.write_file('combo.txt', str(combo))
    
    #update
    update(pet, player)
    player = Player(player_data['name'], player_data['image'], player_data['score'], player_data['badges'])
    
    # make displayable content
    menu_content = [('Learn','learningmode', 'button_learn.png'),('items','/inventory', 'button_inventory.png'),('Buy','/buy', 'button_buy.png'),('words', '/wordlist', 'button_words.png'),('Player','/settings', 'button_settings.png')]
    # change show_badges to either show bades in progress, and if there are none, show what badges could be progressed
    if player.progressing_badges == []:
        show_badges = player.possible_badges
    else:
        show_badges = player.progressing_badges
    # show result
    return template('result_writing', menu=menu_content, badges=show_badges, result=result, question=question, answer=answer, user_input=user_input, points=points, combo=combo, score=player.score, vocs_due=len(duelist), vocs_wait=len(waitlist), vocs_all=len(duelist)+len(waitlist))

if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
