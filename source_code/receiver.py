#This is intended to be a subprocess. It's controlled from another place and receives data.

import time
import os
import signal


os.kill(9636, signal.SIGABRT)

for cnt in range(600):
    data_file = open("synchro.txt", mode="r", encoding="UTF-8")
    current_time = str(data_file.read())
    data_file.close()
    print("Read No {:>3} : {}".format(str(cnt), current_time))
    time.sleep(1.0)
