from datetime import datetime
import time
from random import *

start_time = datetime.now()


def split_list(grade):
    return ([i for i in sorted(grade)if i <= sum(grade)/len(grade)], [i for i in sorted(grade) if i > sum(grade)/len(grade)])


split_list(sample(range(1, 10000001), 1000))

time.sleep(1)
print(datetime.now() - start_time)

