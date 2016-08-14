class Status:
    def __init__(self, name, value, img_list):
        self.name = name 
        self.value = value
        self.maxvalue= 100
        self.image_list = img_list
        
    def decrease_attribute(self, obj):
        if self.value > 0:
            self.value -= 1
        else:
            print('changing states!')
            self.change_status(obj)
    
    #def change_status(self, obj):
    #    pass
        
class Hungry(Status):
    def __init__(self, name, value, image_list):
        super().__init__(name, value, image_list)
    
    def change_status(self, obj):
        obj.status = self 
        obj.image_list = self.image_list
        print(self.image_list)
        print("Hey! I am hungry!")

    
class Normal(Status):
    def __init__(self, name, value, image_list):
        super().__init__(name, value, image_list)
        
    def decrease_attribute(self, obj):
        pass  # soll nicht normal werden wenn zeit abläuft!
    
    def set_normal(self, obj):
        # set status 
        obj.status = self
        obj.image_list = self.image_list
        print("Hello! I am fine!")
        
normal = Normal('normal', 10, ["dummy.png", "dummy01.png", "dummy02.png"])
hungry = Hungry('hungry', 10, ["hungry.png","hungry01.png"])
