from operator import itemgetter

data = [('a',1,'acb'),('c', 13, 'lol'),('b', 0, 'eh'),('d', 4, 'Affe'),('f', 8, 'Keks'),('f', 8, 'Keks'),('f', 4, 'huh?')]
output = sorted(data, key=itemgetter(2))
#for element in output:
#    print (element)

my_dict={}
for element in output:
    print(element)
    if element[0] in my_dict.keys():
        print(element)
        my_dict[element[0]].append(element)
    else:
        my_dict[element[0]] = []
        my_dict[element[0]].append(element)
print(my_dict)
        
'''
# todo: group data
levels = {}
for element in output:
    if element[3] in levels.keys():
        print("alredy there:", element[3])
        key = 'score_{}'.format(element[3])
        levels[key].append(element)
    else:
        key = 'score_{}'.format(element[3])
        levels[key] = []
        levels[key].append(element)
print(levels)'''
