class Voc:
    def __init__(self, question, meaning, hint, lesson, language, answered_corrcetly_counter, answered_counter, time_last_answered, due_time):
        self.question = question
        self.meaning = meaning
        #self.imagepath = None # exculed until I know how to upload data to bottle-server
        self.hint = hint
        #self.tags = tag_list #excluded until I find a good way to store player_tags per player
        self.lesson = lesson
        self.language = language  
        self.answered_correctly_counter = answered_corrcetly_counter
        self.answered_counter = answered_counter  
        self.time_last_answered = time_last_answered
        self.due_time = due_time
        self.is_due_in = None
