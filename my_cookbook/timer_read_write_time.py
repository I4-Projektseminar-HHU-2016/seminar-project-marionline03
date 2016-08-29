import time
import datetime
import json 
# frei nach:
# automate the boring stuff chapter 15 + json in der python doku

current_time = time.time()
print("The Time is ", datetime.datetime.fromtimestamp(current_time))

add_on= input('how many seconds to wait? sec: ')

with open("time.txt", 'w') as data:
    current_time += int(add_on) 
    data.write(str(current_time))

input('Continue?') #wait here

with open('time.txt', 'r') as data:
    imported_data = data.read()
    a = float(imported_data)
    b = datetime.datetime.fromtimestamp(a)
    print("imported time is ",b)

# compare time events
while time.time() <= a:
    print(time.time())
    print(a)
    print('waitig for event')
    # how long to wait?
    time_to_wait = a - time.time()
    #print('Event is in {} seconds'.format(time_to_wait))
    readable_time = datetime.datetime.fromtimestamp(time_to_wait)
    
    #TODO: how to get hours, mins + sec from datetime.datetime.object?
    print(type(readable_time))
    print('Event is in {}'.format(readable_time))
    input('continue?')
else:
    print(time.time())
    print(a)
    print('Event already happend')
    
# datetime.datetime.fromtimestamp(value)
# datetime.datetime.fromtimestamp(time.time())
