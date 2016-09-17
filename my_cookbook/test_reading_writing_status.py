#from pet import Pet
#import datamanager
from status import Hungry, Normal, hungry, normal
#pet = Pet()
import json

def read_json_data(filepath):
    with open(filepath, 'r') as json_data:
        data=json.load(json_data)
        for element in data.items():
            #print("{}:{}--{}".format(type(element[1]), element[0], element[1]))
            return data  
    
def write_json_data(filepath, data):    
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file)

# test: 

'''    def __init__(self, name, value, img_list):
        self.name = name 
        self.value = value
        self.maxvalue= 100
        self.image_list = img_list
'''

# writing status obj
def status_writedown(state):
    name = state.name 
    value = state.value
    maxvalue = state.maxvalue
    image_list = state.image_list
    state_dict = {'name':name, 'value':value, 'maxvalue':maxvalue, 'image_list':image_list}
    return state_dict

hungry_dict = status_writedown(hungry)

# export
write_json_data("test_hungry_dict.json", hungry_dict) 

# reading status obj
read_data = read_json_data("test_hungry_dict.json")
print(read_data)
if read_data == hungry_dict:
    print('everything okay!')
# works  fine :D

# make classes:
def make_normal_obj(status_dict):
    normal = Normal(status_dict['name'],status_dict['value'], status_dict['image_list'])
    return normal

def make_hungry_obj(status_dict):
    hungry = Hungry(status_dict['name'],status_dict['value'], status_dict['image_list'])
    return hungry
    
hungry2= make_hungry_obj(read_data)
if hungry == hungry2:
    print("okay :)")
else:
    print('hungry != hungry2... manual check ...')
    print(hungry.name, hungry2.name)
    print(hungry.value, hungry2.value)
    print(hungry.image_list, hungry2.image_list)
    print(hungry.image_list[0], hungry2.image_list[0])
