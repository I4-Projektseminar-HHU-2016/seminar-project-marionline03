import time
import datetime
import json 
# frei nach:
# automate the boring stuff chapter 15 + json in der python doku

# Zeit lesen und schreiben als txt datei

# Zeit wird in json-Datei geschrieben
# Zeit wird beim nächsten Start eingelesen

current_time = time.time()
print("The Time is ", datetime.datetime.fromtimestamp(current_time))

with open("time.txt", 'w') as data: 
    data.write(str(current_time))

input('Continue?') #wait here

with open('time.txt', 'r') as data:
    imported_data = data.read()
    print(imported_data)
    print("time is ", datetime.datetime.fromtimestamp(current_time))
    a = float(imported_data)
    print(a)
    print("imported time is ", datetime.datetime.fromtimestamp(a))

    
