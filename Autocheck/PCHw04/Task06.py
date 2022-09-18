from datetime import datetime
import time
from random import *
x = sample(range(1, 10000001), 5000)
start_time = datetime.now()


def split_list(grade):
    return ([i for i in sorted(grade)if i <= sum(grade)/len(grade)], [i for i in sorted(grade) if i > sum(grade)/len(grade)])


split_list(x)

time.sleep(1)
print(datetime.now() - start_time)