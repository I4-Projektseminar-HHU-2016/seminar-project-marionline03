# Sources used:  
# Bottle Doku: bottlepy.org/docs/dev/index.thml

import random
import bottle
from bottle import route, run, template, static_file
from do_not_upload import STATIC_FILES_PATH
from read_write_csv import Datamanager
from pet import Pet
from player import Player

INTERVAL = 1000  # how fast the page reloads - in miliseconds  


#lookes ugly, maybe just reload part of webpage?
# -> stackoerflow: http://stackoverflow.com/questions/12399952/only-reload-a-part-of-a-web-page

datamanager = Datamanager()

def update(pet, player):
    # after the data is loaded, 
    # update calls the classes updatefunctions
    pet.change_status()
    pass


@route('/inventory')
def show_inventory():
    #player.get_inventory()
    pass
    
# if user klicks something
@route('/inventory', method='POST')
def handle_inventory_event():
    # get from input
    pass
    # what form input? use, delete? 
    
    # on item use 
        #return #gamescreen #with eating monster animation
    # on item deletion  
        #return #inventory
       
@route('/wordlist')
def show_wordlist():
    # request voc data
    
    # make displayable voc data
    
    return template('table goes here')

@route('/<filename>')
def serve_static(filename):
    return static_file(filename, root=STATIC_FILES_PATH)

@route('<filename>')
def give_static(filename):
    return static_file(filename, root='/static/')

@route('/')
def hello():
    # everything should be re-routed to hello when there is no data set
    #TODO: handle Exception if file not found
    player_data = datamanager.read_json_data('player.json')
    pet_data = datamanager.read_json_data('pet.json')
    
    #create objects 
    pet = Pet(pet_data['name'], pet_data['hp'], pet_data['status'], pet_data['image'], pet_data['imagelist'], pet_data['level'], pet_data['exp'])
    player = Player(player_data['name'], player_data['image'], player_data['score'], player_data['badges'])
    
    #update
    update(pet, player)
        
    # set images etc.
    pet_image = set_pet_image(pet.image_list)
    
    # export
    known_states = []
    for element in pet.known_states.keys():
        status_dict = {"name":pet.known_states[element].value, "value":pet.known_states[element].value, "image_list":pet.known_states[element].image_list}
        known_states.append(status_dict) 
    pet_dict = {"name": pet.name, "hp":pet.hp, "known_states":known_states, "status": pet.status.name, "hungry_in": pet.status.value, "image": pet.image, "imagelist":pet.image_list, "level": pet.level, "exp":pet.exp} 
    datamanager.write_json_data('pet.json', pet_dict)
    menu_content = [('Learn','/learnmode', 'button_learn.png'),('items','/inventory', 'button_inventory.png'),('Buy','/buy', 'button_buy.png'),('words', '/wordlist', 'button_words.png'),('Player','/settings', 'button_settings.png')]
    return template('page', interval=INTERVAL, menu=menu_content, pet_image=pet_image, badges=player.badges, pet_status=pet.status.name, pet_hunger=pet.known_states['hungry'].value)

@route('/pet_image')
def set_pet_image(data_list):
    return random.choice(data_list)    
      
run(host='localhost', port=8080, reloader=True)
