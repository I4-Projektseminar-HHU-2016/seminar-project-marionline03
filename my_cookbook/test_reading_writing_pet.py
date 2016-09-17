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
        #print(element)
        stateobj_as_dict = status_writedown(element[1])
        list_of_status_dicts.append({element[0]:stateobj_as_dict})
    pet_dict = {'name':pet.name, 'hp':pet.hp, 'status':pet_status_dict, 'known_states':list_of_status_dicts, 'image':pet.image, 'image_list':pet.image_list}
    #print(pet_dict)
    write_json_data("test_pet_data.json", pet_dict)
    return pet_dict

output =  write_pet_data(pet)

def import_pet(filepath):
    data = read_json_data(filepath)
    return data

def import_and_make_pet_obj(filepath):
    data = read_json_data(filepath)
    #print(data)
    #print(len(data))
    return data



#TEST 1
################
# import data and original compared
################
'''filepath ="test_pet_data.json"
imported_data = import_pet(filepath)
if imported_data == output:
    print('alles okay')
else:
    print(output)
    print(imported_data)'''

#TEST 2
########################
# print single element 
##########################
'''filepath ="test_pet_data.json"
output = import_and_make_pet_obj(filepath)
for element in output.items():
    print(element)'''

# Test 3
###########################
# import and make objects
###########################
filepath ="test_pet_data.json"
output = import_and_make_pet_obj(filepath)
name = output['name']
hp = output['hp']

if output['status']['name'] == 'normal':
    #make normal obj
    state_obj = make_normal_obj(output['status'])
elif output['status']['name'] == 'hungry':
    #make hungry obj
    state_obj = make_hungry_obj(output['status'])

def make_know_states_obj(known_state_element):
    print('make_know_states_obj: ', known_state_element)
    if output['status']['name'] == 'normal':
        #make normal obj
        state_obj = make_normal_obj(output['status'])
    elif output['status']['name'] == 'hungry':
        #make hungry obj
        state_obj = make_hungry_obj(output['status'])

status = state_obj
#TODO
known_states_dict = {}
print(known_states)
print(known_states.items())
for element in known_states.items(): 
    print("..", element)
    state = make_know_states_obj(element)
    print(state)
    known_states[element[0]] = state
print(known_states_dict)
#print(my_list)

image = output['image']

image_list= output['image_list']

level=0

exp=0



