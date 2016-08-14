from status import status

class pet():
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.hunger_counter = 100
        self.status = normal
        self.image = 'normal.png'
        self.level = 0
        self.exp = 0
    
    def change_status(status):
        pass   
        
    def change_name(name):
        self.name = name
