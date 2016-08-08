import time
import datetime

# frei nach:
# automate the boring stuff chapter 15

# jede Sekunde wird die Zeit geprintet

a = time.time()
print("a is ", a)
print("time is ", round(time.time()))

lasttime = round(time.time())
while True:
    if round(time.time()) != lasttime:
        print(round(time.time()))
        lasttime= round(time.time())
