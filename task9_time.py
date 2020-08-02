from task5_top_ten_movie import *
import random
import time
def runtime():
    for count in ten_movies_list:
        any_num = (random.randint(1,3))
        print(any_num)
        time.sleep(any_num)
runtime()

total_time = time.time()
print(total_time)