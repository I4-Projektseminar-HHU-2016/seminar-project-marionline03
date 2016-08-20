class Player():
    def __init__(self, name, image, score, badges):
        self.name = name
        self.image = image
        self.score = score
        self.possible_badges = badges
        self.has_badges = []
        self.progressing_badges  = []
        
    def change_name(name):
        pass

    def increase_scrore(self, amount):
        self.score += amount
        
    def get_badge(self, badge):
        #badge.check() <- badge checks for following badges, e.g. badge A hat a A2 Badge that follows
        pass
    
    def change_image(self, imagefile):
        pass
