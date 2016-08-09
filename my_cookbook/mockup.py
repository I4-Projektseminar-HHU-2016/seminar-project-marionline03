# Sources used:  
# Bottle Doku: bottlepy.org/docs/dev/index.thml

import bottle
from bottle import route, run, template, static_file
from do_not_upload import STATIC_FILES_PATH

@route('/<filename>')
def serve_static(filename):
    return static_file(filename, root=STATIC_FILES_PATH)

@route('<filename>')
def give_static(filename):
    return static_file(filename, root='/static/')

@route('/')
def hello():
    return template('page', menu=[('Words','a'),('Pet','b'),('Items','c'),('Player','d')], heading='Hello world =D!', content='bla bla bla')

run(host='localhost', port=8080, reloader=True)
