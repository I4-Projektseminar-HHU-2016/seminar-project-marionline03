import csv
import json
#import player

class Datamanager():
    def __init__(self):
        pass
    
    def read_json_data(self, filepath):
        with open(filepath, 'r') as json_data:
            data=json.load(json_data)
            for element in data.items():
                print("{}:{}--{}".format(type(element[1]), element[0], element[1]))
                return data  
        
    def write_json_data(self, filepath, data):    
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file)
        
    def read_csv_data(self, filepath):
        with open(filepath, 'r') as file_data:
            reader = csv.reader(file_data, delimiter=";")
            next(reader) # skips first row, wich is used for collumn names
            # parse data
            for row in reader:
                print(row)
            return reader
        
    def write_csv_data(self, filepath, data):    
        with open(filepath, 'w') as file_data:
            writer  = csv.writer(file_data, delimiter=';')
            writer.writerows(data)
    
data_manager = Datamanager()
#write_list=[['Name','Image','Score','Badges'],['Player','path/to/image','0', [] ]]
#data_manager.write_csv_data("player.csv", write_list)
#data_manager.read_csv_data('player.csv')
#write_dict = {"name":"Player", "image":"path/to/image", "score":0, "badges":['A', 'B', 'C']}
#write_pet_dict = {"name":"Alien", "image":"dummy.png", 'imagelist':['dummy.png','dummy01.png','dummy02.png'],"level":0, "exp":0, "hungry_in":100, "state":'normal'}
#data_manager.write_json_data('pet.json', write_pet_dict)
#data_manager.write_json_data('player.json', write_dict)
#data_manager.read_json_data('player.json')
