from bottle import Bottle, route, run, template, debug
import time
import datetime

# Threads? :(
import thread
# import thread # http://www.tutorialspoint.com/python/python_multithreading.htm
#thread.start_new_thread ( function, args[, kwargs] )


class Observer:
    def __init__(self):
        pass 
    
    def receive(self, data):
        print("I got {}".format(data))


class Subject():
    def __init__(self):
        self.clients = []

    def send(self, data):
        for client in self.clients:
                client.receive(data)
                
    def remove_client(self, client):
        self.clients.remove(client)   
    
    def add_client(self, client):
            self.clients.append(client)
        
        
# frei nach:
# automate the boring stuff chapter 15
# jede Sekunde wird die Zeit geprintet

class Timer(Subject):
    def __init__(self):
        super().__init__()
        self.clients = []
        self.lasttime = round(time.time())

    def run(self):
        while True:
            if round(time.time()) != self.lasttime:
                self.lasttime= round(time.time())
                self.send(self.lasttime)

##read: http://stackoverflow.com/questions/8725605/bottle-framework-and-oop-using-method-instead-of-function
class MyApp(Bottle):
    def __init__(self, name):
        super(MyApp, self).__init__()
        self.name = name
        self.time=time.time()
        self.route('/', callback=self.index)
        self.route('/hello', callback=self.hello)
    
    def index(self):
        return "Hello, my name is " + self.name
        
    def receive(self, data):
        print("data: ",data)
        self.hello(self.time)
        
    def hello(self, time=time.time()): 
        return '<h1>hello world =D!<br> {}</h1>'.format(time)  

if __name__ == '__main__':
    app = MyApp('My-App')
    # Hier: Timer-Klasse im neuen Thread starten: timer = Timer()
    timer.add_client(app)
    timer.send('test')
    
    # diese beiden run befehle blockieren sich gegenseitig. Juhuu! -_-
    app.run(host='localhost', port=8080)
    timer.run() 
    # wird nicht angezeigt ...
    timer.send('test 02')
