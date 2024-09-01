import time
print(f"GMT: {'%c',time.gmtime(0)}")
print(f"Time zone: {time.tzname[0]}, offset: {time.timezone}")

time_now = time.strftime(f'{time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())}')
print(time_now)