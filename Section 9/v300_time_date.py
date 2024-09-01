import time
from time import time as my_timer
import random

input("Press enter to start...")
wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop...")
end_time = my_timer()

print(f"Your start time {time.strftime("%X", time.localtime(start_time))}")
print(f"Your end time {time.strftime("%X", time.localtime(end_time))}")
print(f"Your reaction time {end_time-start_time} seconds")