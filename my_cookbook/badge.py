class Badge():
    def __init__(self, name, description, image, has_player_badge, action_list, progress_per_action):
        self.name = name
        self.decription = description
        self.image = image
        self.is_archieved_by_player = has_player_badge     
        self.player_progress_for_badge = 0
        self.action = action_list # list with actions that trigger progress on badge, they are stored as string, but could be made classes as well
        self.progress_per_action = progress_per_action
    
    #TODO: test if works 
    # Badge observes Player's action
    def on_player_action(self, player):
        if self.does_player_get_badge(player):
            self.receive_badge(player)
        else:
            player_progress_for_badge +=1         
    
    def receive_badge(self, player):
        # give player the badge
        player.possible_badges.pop(self)
        player.badges.append(self)
    
    def does_player_get_badge(self, player): 
    # test if player
        if self.player_progress == 100 and self.is_archieved_by_player == False:
            self.is_archieved_by_player = True
            return True
        else:
            return False
            
welcome_badge = Badge('welcome!','create an account','path/to/image', False, ['start-playing'], 100)
gave_10_berries_to_pet = Badge('caretaker','gave 10 berries to pet','path/to/image',False, ['feed_item'], 10)
