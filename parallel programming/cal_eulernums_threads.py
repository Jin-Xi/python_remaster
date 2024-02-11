import random
import time
from threading import Thread
import os
from numba import jit, int32


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time} seconds to execute.")
        return result
    return wrapper


class CAL_e:
    def __init__(self, iterations: int):
        self.n = 0
        self.iterations = iterations * int(os.cpu_count()/4)

    @time_decorator
    def mimic(self):
        for _ in range(self.iterations):
            tmp_sum = random.uniform(0, 1)
            count = 1
            while True:
                tmp_sum += random.uniform(0, 1)
                count += 1
                if tmp_sum >= 1:
                    self.n += count
                    break

    def get_natural_number(self):
        return self.n / self.iterations


if __name__ == '__main__':
    # 计算3000w次
    e = CAL_e(30000000)
    threads_list = []
    for i in range(int(os.cpu_count()/4)):
        t = Thread(target=e.mimic)
        t.start()
        threads_list.append(t)
        print("thread %d starting" % i)
    for i, s in enumerate(threads_list):
        s.join()
        print("thread %d joining" % i)

    # e.mimic()
    print(" the e is %.10f" % e.get_natural_number())
