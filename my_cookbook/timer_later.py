import datetime
import time

## automate the boring stuff chapter 15

one_second_later = datetime.datetime.now() + datetime.timedelta(seconds=1)
while datetime.datetime.now() < one_second_later:
    time.sleep(1)
print("Pling!")
