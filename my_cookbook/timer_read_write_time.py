import time
import datetime
import json 
# frei nach:
# automate the boring stuff chapter 15 + json in der python doku

current_time = time.time()
print("The Time is ", datetime.datetime.fromtimestamp(current_time))

add_on= input('how many sce to wait?')

with open("time.txt", 'w') as data:
    current_time += int(add_on) 
    data.write(str(current_time))

input('Continue?') #wait here

with open('time.txt', 'r') as data:
    imported_data = data.read()
    a = float(imported_data)
    b = datetime.datetime.fromtimestamp(a)
    print("imported time is ",b)

# do maths 
#datetime.datetime.fromtimestamp(a)
while time.time()<= a:
    print(time.time())
    print(a)
    print('waitig for event')
    input('continue?')
else:
    print(time.time())
    print(a)
    print('Event already happend')
    
# datetime.datetime.fromtimestamp(value)
# datetime.datetime.fromtimestamp(time.time())
