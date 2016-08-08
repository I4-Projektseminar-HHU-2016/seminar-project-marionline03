class Status:
    def __init__(self, name)
        self.name = name 
        
    def change_attributes(self):
        pass

class Hungry(Status):
    super()__init__(name)
    
    def  change_attributes(self, obj):
            obj.status = self.name 
            obj.img = 'hungry.png'

normal = Status('normal')
hungry = Status('hungry')
