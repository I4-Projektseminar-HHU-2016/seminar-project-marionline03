from status import normal, hungry

class Pet():
    def __init__(self, name, hp, status, image, imagelist, level=0, exp=0):
        self.name = name
        self.hp = 100
        self.known_states = {'hungry':hungry} #List with active states
        self.status = normal
        self.image = image
        self.image_list = imagelist
        self.level = 0
        self.exp = 0
    
    def change_status(self):
        for status in self.known_states.keys(): 
            self.known_states[status].decrease_attribute(self)  
        
    def change_name(self, name):
        self.name = name
    
    def receive_food(self, food):
        # TODO: think about this,  at the momement each new state needs such a function
        self.known_states['hungry'].value += food.value
