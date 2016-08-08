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
        #TODO: wie löscht man nochmal elemente aus listen?  
        pass
        
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
