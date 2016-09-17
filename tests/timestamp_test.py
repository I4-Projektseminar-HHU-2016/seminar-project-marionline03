# http://stackoverflow.com/questions/2775864/python-create-unix-timestamp-five-minutes-in-the-future
import time
import datetime
import os

current_time = datetime.datetime.now(datetime.timezone.utc)
unix_timestamp = current_time.timestamp() # works if Python >= 3.3

unix_timestamp_plus_5_min = unix_timestamp + (1 * 10)  # 5 min * 60 seconds

# http://unix.stackexchange.com/questions/1974/how-do-i-make-my-pc-speaker-beep
# http://stackoverflow.com/questions/6537481/python-making-a-beep-noise
# https://askubuntu.com/questions/19906/beep-in-shell-script-not-working
# http://billposer.org/Linguistics/Computation/SoxTutorial.html
#http://stackoverflow.com/questions/4467240/play-simple-beep-with-python-without-external-library
def beep():
    os.system('play -n sine.wav synth 2.0 square  500.0')


while time.time() < unix_timestamp_plus_5_min:
    time.sleep(1)
beep()

