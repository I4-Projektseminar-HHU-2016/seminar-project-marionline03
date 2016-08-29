import csv
import json
import time

class Datamanager():
    def __init__(self):
        pass
    
    def make_hash():
        ''' some insecure hashing function to prevent player from reading answer'''
        pass 
    
    def read_file(self, filepath):
        with open(filepath, 'r') as data_file:
            data = data_file.read()
            return data
            
    def write_file(self, filepath, data):
        with open(filepath, 'w') as data_file:
            data_file.write(data)    
       
    def read_json_data(self, filepath):
        with open(filepath, 'r') as json_data:
            data=json.load(json_data)
            for element in data.items():
                #jzint("{}:{}--{}".format(type(element[1]), element[0], element[1]))
                return data  
        
    def write_json_data(self, filepath, data):    
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file)
        
    def read_csv_data(self, filepath):
        with open(filepath, 'r') as file_data:
            reader = csv.reader(file_data, delimiter='|')
            next(reader) # skips first row, wich is used for collumn names
            voc_list = []
            for row in reader:
                #print(row)
                voc_list.append(row)
            return voc_list
        
    def write_csv_data(self, filepath, data, datacodeing):    
        with open(filepath, 'w') as file_data:
            # https://docs.python.org/3/library/csv.html
            fieldnames = datacodeing
            writer = csv.DictWriter(file_data, fieldnames=fieldnames, delimiter='|')
            writer.writeheader()
            for element in data:
                writer.writerow(element)

data_manager = Datamanager()
#question, meaning, hint, lesson, language, answered_corrcetly_counter, answered_counter, time_last_answered

#voc_f = {'question':'Bonjour','meaning':'hello','hint':'','lesson':'French Words','language':'French','answered_corrcetly_counter':0,'answered_counter':0, 'time_last_answered':str(time.time()), 'due_time': str(time.time())}
#voc_g = {'question':'Guten Tag','meaning':'hello','hint':'','lesson':'German Words','language':'German','answered_corrcetly_counter':0,'answered_counter':0, 'time_last_answered':str(time.time()), 'due_time':str(time.time())}
#voc_c = {'question':'你好','meaning':'hello','hint':'Nǐhǎo','lesson':'Chinese Words','language':'Chinese','answered_corrcetly_counter':0,'answered_counter':0, 'time_last_answered':str(time.time()), 'due_time':str(time.time())}

#data_manager.write_csv_data('voc.csv', [voc_f,voc_g,voc_c])
#data_manager.write_csv_data( 

#test_data = data_manager.read_csv_data('voc.csv')
#write_list=[['Name','Image','Score','Badges'],['Player','path/to/image','0', [] ]]
#data_manager.write_csv_data("player.csv", write_list)
#data_manager.read_csv_data('player.csv')
#write_dict = {"name":"Player", "image":"path/to/image", "score":0, "badges":['A', 'B', 'C'], 'has_badges':[], 'progressing_badges':[], 'inventory':[]}
#write_pet_dict = {"name":"Alien", "hp":100, "image":"dummy.png", 'imagelist':['dummy.png','dummy01.png','dummy02.png'],"level":0, "exp":0, "hungry_in":100, "status":'normal'}
#data_manager.write_json_data('pet.json', write_pet_dict)
#data_manager.write_json_data('player.json', write_dict)
#data_manager.read_json_data('player.json')
