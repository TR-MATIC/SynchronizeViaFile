#This is intended to be the main process. It controls others and gives the data feed.

import time
import os

for cnt in range(6000):
    current_time = time.strftime("%H:%M:%S")
    data_file = open("synchro.txt", mode="w", encoding="UTF-8")
    data_file.write(current_time)
    data_file.close()
    if not (cnt % 10):
        print("{:>4}/".format(str(cnt)), end="")
    time.sleep(0.1)
    if not (cnt % 250):
        print("\n >> {} <<".format(os.getpid()))
