# Versuch das Observerpattern umzusetzen über das GUI und Controller kommunizieren sollen.

class Observer:
    def __init__(self, name):
        self.name = name
        pass 
    
    def receive(self, data):
        print("{}: I got {}".format(self.name, data))


class Subject():
    def __init__(self, name):
        self.name = name
        self.clients = []

    def send(self, data):
        for client in self.clients:
            if client isinstance(Observer): # isinstance
                client.receive(data)
            
    def remove_client(self, client):
        # http://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value-in-python
        self.clients.remove(client)
        
    def add_client(self, client):
        if client isinstance(client, Observer):
            self.clients.append(client)
        else:
            raise TypeError    
        
a = Observer('A')
b = Subject('B')
b.add_client(a)
b.send('bla bla')
b.add_client(Observer('C'))
b.send("lala Laa!")
