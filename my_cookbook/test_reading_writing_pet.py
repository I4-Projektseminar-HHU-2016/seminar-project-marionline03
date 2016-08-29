# test read write pet data

from pet import Pet
import json
from status import normal, hungry
from test_reading_writing_status import status_writedown, make_hungry_obj, make_normal_obj
#from status import normal, hungry

name = 'test_pet'
hp = 1000
status = normal
known_states = {'hungry':hungry, 'normal':normal}
image = 'dummy.png'
image_list = ['dummy.png']
 
pet = Pet(name, hp, status, known_states, image, image_list, level=0, exp=0)
print(pet)
print(pet.name)

def read_json_data(filepath):
    with open(filepath, 'r') as json_data:
        data=json.load(json_data)
        for element in data.items():
            return data  
    
def write_json_data(filepath, data):    
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file)

def write_pet_data(pet):
    pet_status_dict = status_writedown(pet.status)
    list_of_status_dicts = []
    for element in known_states.items():
        print(element)
        stateobj_as_dict = status_writedown(element[1])
        list_of_status_dicts.append({element[0]:stateobj_as_dict})
    pet_dict = {'name':pet.name, 'hp':pet.hp, 'status':pet_status_dict, 'known_states':list_of_status_dicts, 'image':pet.image, 'image_list':pet.image_list}
    print(pet_dict)
    write_json_data("test_pet_data.json", pet_dict)
    return pet_dict

output =  write_pet_data(pet)

def import_pet():
    data = read_json_data("test_pet_data.json")
    print(data)
    return data

imported_data = import_pet()
if imported_data == output:
    print('alles okay')
else:
    print(output)
    print(imported_data)
