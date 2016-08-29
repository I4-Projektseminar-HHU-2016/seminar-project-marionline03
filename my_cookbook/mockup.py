# Sources used:  
# Bottle Doku: bottlepy.org/docs/dev/index.thml

# reload part of webpage:
# -> stackoerflow: http://stackoverflow.com/questions/12399952/only-reload-a-part-of-a-web-page

# exceptions: 
#found here: http://www.tutorialspoint.com/python/python_exceptions.htm    

import random
import bottle
from bottle import route, run, template, static_file, request, redirect
from do_not_upload import STATIC_FILES_PATH
from read_write_csv import Datamanager
from pet import Pet
from player import Player
from badge import BADGES #Badge, welcome_badge, gave_10_berries_to_pet # <- !
import time
from voc import Voc
from food import berry, raspberry
from status import Hungry, Normal
INTERVAL = 700  # how fast the page reloads - in miliseconds  

datamanager = Datamanager()

def make_status_obj(status_dict):
    print(status_dict)
    if status_dict['name'] == 'hungry':
        hungry = Hungry(status_dict['name'],status_dict['value'], status_dict['image_list'])
        return hungry
    elif status_dict['name'] == 'normal':
        normal = Normal(status_dict['name'],status_dict['value'], status_dict['image_list'])
        return hungry

def make_status_dict(state):
    name = state.name 
    value = state.value
    maxvalue = state.maxvalue
    image_list = state.image_list
    state_dict = {'name':name, 'value':value, 'maxvalue':maxvalue, 'image_list':image_list}
    return state_dict

def make_badges_dict(badges,has_badges,progressing_badges):
    all_badges = badges + has_badges + progressing_badges
    print(all_badges)
    badge_list = []
    # make dic
    if len(all_badges) < 1:
        print('make_badges_dict: No badges found!')
        #TODO
        # raise Error 
    for badge in all_badges:
        #name, description, image, has_player_badge, action_list, progress_per_action
        badges_dict = {}
        badges_dict['name'] = badge.name
        badges_dict['description'] = badge.description
        badges_dict['image'] = badge.image
        badges_dict['has_player_badge'] = badge.has_player_badge
        badges_dict['action_list'] = badge.action_list
        badges_dict['progress_per_action'] = badge.progress_per_action
        badge_list.append(badges_dict)
    return badges_dict

def find_voc(question, duelist):
    # would be good to make voc have an id to indentify them, instead by question...
    for voc in duelist:
        if voc.question == question:
            return voc

def make_player_dict(player):
    player_dict = {}
    player_dict['name'] = player.name
    player_dict['image'] = player.image
    player_dict['score'] = player.score
    player_dict['badges'] = player.possible_badges 
    player_dict['has_badges'] = player.has_badges
    player_dict['progressing_badges'] = player.progressing_badges    
    player_dict['inventory'] = player.inventory 
    return player_dict 

def make_voc_dict(duelist, waitlist):
    voc_list = duelist + waitlist
    voc_data = []
    for voc in voc_list:
        voc_to_save ={'question':voc.question, 'meaning':voc.meaning, 'hint':voc.hint, 'lesson':voc.lesson, 'language':voc.language, 'answered_corrcetly_counter':voc.answered_correctly_counter, 'answered_counter':voc.answered_counter, 'time_last_answered':voc.time_last_answered, 'due_time': voc.due_time}
        voc_data.append(voc_to_save)
    for element in voc_data:
        print("make_voc_dict: ", element)
    return voc_data

def sort_vocabulary_by_due_time(vocs):
    duelist = [] # these vocs will be asked
    waitlist = [] # are not to be asked now, asked later
    
    # Todo: how to filter these? by due_time = 0?
    # unseen_list = [] # where never asked before, new/unseen
    
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

def load_data():
    try:
        player_data = datamanager.read_json_data('player.json')
        pet_data = datamanager.read_json_data('pet.json')
        voc_data = datamanager.read_csv_data('voc.csv')
    # found here: http://www.tutorialspoint.com/python/python_exceptions.htm    
    # TODO: if file not found, ask for filepath and/or offer option to create a new file
    except IOError:
        return "Error: can\'t find file or read data"
    
    #create objects 
    status=make_status_obj(pet_data['status'])
    pet = Pet(pet_data['name'], pet_data['hp'], status, pet_data['image'], pet_data['imagelist'], pet_data['level'], pet_data['exp'])
    player = Player(player_data['name'], player_data['image'], player_data['score'], [], [], [], player_data['inventory'])
    if player_data['has_badges'] == None:
        player_data['has_badges'] = []
    else:
        if type(player_data['has_badges']) == str:
            player_data['has_badges'] = player_data['has_badges'].split()
        for element in BADGES:
            if element.name in player_data['has_badges']:
                player.has_badges.append(element)
    
    if player_data['progressing_badges'] == None:
        player_data['progressing_badges'] = []
    else:
        if type(player_data['has_badges']) == str:
            player_data['has_badges'] = player_data['has_badges'].split()
        for element in BADGES:
            if element.name in player_data['progressing_badges']:
                player.progressing_badges.append(element)
    
    print("possible badges: ", player.possible_badges)
    print("badges player owns: ", player.has_badges)
    print("badges player is progressing on: ", player.progressing_badges)
    
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
    return (player, pet, duelist, waitlist)

def give_food_items_to_pet():
    pass

def make_badge(bagde_data):
    #TODO
    # data needs to be csv. 
    # This only works for sigle player mode: 
    # Each badge has data about: name, description, image, has_player_badge, action_list, progress_per_action
    # parse data
    for element in bagde_data:
        name = element[0]
        description = element[1]
        image = element[2]
        has_player_badge = element[3]
        action_list = element[4]
        assert(type(actionlist == list))
        progress_per_action = element[5] 
    badge = Badge(name, description, image, has_player_badge, action_list, progress_per_action) 
    return badge


def update_badges(player):
    # change show_badges to either show bades in progress, and if there are none, show what badges could be progressed
    if player.progressing_badges == []:
        show_badges = player.possible_badges
    else:
        show_badges = player.progressing_badges
    return show_badges

def update(pet, player):
    # after the data is loaded, 
    # update calls the classes update-functions
    pet.change_status()

def update_vocabulary(duelist, wait_list):
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
    player, pet, duelist, waitlist = load_data()
    
    #create badges that player still can arcieve they are imported from badges.py, but could be created here as well, 
    
    #TODO 
    # create badges here means to import their data from player.json or somewhere else!
    update_badges(player)
    
    #TODO 
    #create items to be put in player's inventory 
    
    #TODO
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
    
    badge_data = make_badges_dict(player.possible_badges ,  player.has_badges , player.progressing_badges)
    datamanager.write_csv_data("badges.cvs", badge_data, ['name', 'description', 'image', 'has_player_badge', 'action_list', 'progress_per_action'])
    # add a message like 'pet ate food'?
    redirect('/')
    
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


@route('/')
def show_index():
    # everything should be re-routed here
    player, pet, duelist, waitlist = load_data()
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
    player_dict =  make_player_dict(player)
    datamanager.write_json_data('player.json', player_dict,)
    # write voc_data 
    voc_data = make_voc_dict(duelist, waitlist)
    datamanager.write_csv_data('voc.csv', voc_data, ['question', 'meaning', 'hint', 'lesson', 'language','answered_corrcetly_counter', 'answered_counter', 'time_last_answered', 'due_time'])
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
    player, pet, duelist, waitlist = load_data()
    # change show_badges to either show bades in progress, and if there are none, show what badges could be progressed
    if player.progressing_badges == []:
        show_badges = player.possible_badges
    else:
        show_badges = player.progressing_badges
    #reset combo
    try:
        combo = datamanager.read_file('combo.txt') # if there is no combo      
    except:
        combo = 0
    if not combo == 0:
        combo = 0
        datamanager.write_file('combo.txt', str(combo))   
    # return template + variables   
    
    learning_mode_list = []
    if len(duelist) > 1:
        learning_mode_list.append(('write','writing test'))
    if len(duelist) > 1:
        learning_mode_list.append(('flash card mode','flash_card'))
    #if len(duelist)  > 3:
    #    learning_mode_list.append(('mulpile choice', 'multiple_choice'))
    #if len(duelist)  > 15:    
    #    learning_mode_list.append(('memory game', 'memory'))
    if len(learning_mode_list) == 0:
        learning_mode_list.append(('/','Currently there are no words foundd, that need learning. You can add words in the wordlist menu. Klick th text to return to main screen!'))

        
    menu_content = [('Learn','learningmode', 'button_learn.png'), ('items','/inventory', 'button_inventory.png'),('Buy','/buy', 'button_buy.png'),('words', '/wordlist', 'button_words.png'),('Player','/settings', 'button_settings.png')]
    return template('choose_learn_method', interval=INTERVAL, menu=menu_content, badges=show_badges, learning_mode=learning_mode_list )
      
@route('/write')
def writing_test():
    player, pet, duelist, waitlist = load_data()
    ask_for_voc = random.choice(duelist)
    # save question, answer in text file for persistence
    # TODO: hash answer , write hash
    datamanager.write_file('answer.txt', ask_for_voc.meaning)
    datamanager.write_file('question.txt', ask_for_voc.question)
    # change show_badges to either show bades in progress, and if there are none, show what badges could be progressed
    show_badges = update_badges(player)
    # make displayable content
    menu_content = [('Learn','learningmode', 'button_learn.png'),('items','/inventory', 'button_inventory.png'),('Buy','/buy', 'button_buy.png'),('words', '/wordlist', 'button_words.png'),('Player','/settings', 'button_settings.png')]    
    return template('writing', menu=menu_content, badges=show_badges, voc=ask_for_voc, vocs_due=len(duelist), vocs_wait=len(waitlist), vocs_all=len(duelist)+len(waitlist))


@route('/write', method='POST')
def writing_mode():
    player, pet, duelist, waitlist = load_data()
    # import voc data, active question, expected answer
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
    # find voc-obj to alter it
    voc = find_voc(question, duelist)
    # evaluate
    result = False
    combo = int(combo)
    #TODO: negative_combo for wrong answers, 16 times false, player get an old toaster - item
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
        voc.answered_correctly_counter += 1
        voc.answered_counter += 1 
        voc.time_last_answered = str(time.time())
        # TODO: repetition algorithm needed: something better than 5*answered_counter
        voc.due_time = str(round(time.time())+5*answered_counter) 
        #TODO: display an image: happy pet
    else:
        combo = 0    
        points = 0
        # TODO: display image: sad pet
    datamanager.write_file('combo.txt', str(combo))
    
    #update
    update(pet, player)
    
    # change show_badges to either show bades in progress, and if there are none, show what badges could be progressed
    show_badges = update_badges(player)
    
    # save voc_data 
    writable_voc_data= make_voc_dict(duelist, waitlist)
    datamanager.write_csv_data('voc.csv', writable_voc_data, ['question', 'meaning', 'hint', 'lesson', 'language','answered_corrcetly_counter', 'answered_counter', 'time_last_answered', 'due_time'])
    player_dict = make_player_dict(player)
    datamanager.write_json_data('player.json', player_dict)
    
    # show result
    menu_content = [('Learn','learningmode', 'button_learn.png'),('items','/inventory', 'button_inventory.png'),('Buy','/buy', 'button_buy.png'),('words', '/wordlist', 'button_words.png'),('Player','/settings', 'button_settings.png')]
    return template('result_writing', menu=menu_content, badges=show_badges, result=result, question=question, answer=answer, user_input=user_input, points=points, combo=combo, score=player.score, vocs_due=len(duelist), vocs_wait=len(waitlist), vocs_all=len(duelist)+len(waitlist))

if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
