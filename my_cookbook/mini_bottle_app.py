# Sorces used:  
# Bottle Doku: bottlepy.org/docs/dev/index.thml

from bottle import route, run, template

@route('/')
def hello():
    return '<h1>hello world =D!</h1>'  

run(host='localhost', port=8080)
