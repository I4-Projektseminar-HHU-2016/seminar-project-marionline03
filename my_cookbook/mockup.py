# Sources used:  
# Bottle Doku: bottlepy.org/docs/dev/index.thml

import bottle
from bottle import route, run, template, static_file
from do_not_upload import STATIC_FILES_PATH

@route('inventory')
def show_inventory():
    pass
    
# if user klicks something
@route('/inventory')
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
    return template('page', 
    menu=[('Learn','/learnmode', 'button_learn.png'),('items','/inventory', 'button_inventory.png'),('Buy','/buy', 'button_buy.png'),('words', '/wordlist', 'button_words.png'),('Player','/settings', 'button_settings.png')], pet_image='dummy.png', content='bla bla bla', badges=['Badge A','Badge B','Badce C', 'Badge D', 'Badge E'])

run(host='localhost', port=8080, reloader=True)
