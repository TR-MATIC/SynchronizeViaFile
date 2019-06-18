#This is intended to be the main process. It controls others and gives the data feed.

import time

for cnt in range(60):
    current_time = time.strftime("%H:%M:%S")
    data_file = open("synchro.txt", mode="w", encoding="UTF-8")
    data_file.write(current_time)
    data_file.close()
    time.sleep(0.5)
