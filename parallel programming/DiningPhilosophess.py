from threading import Thread, Lock
import random
import time


class DiningPhilosophess:
    def __init__(self, num_of_phi, num_of_chopsticks):
        self.meals = [7 for _ in range(num_of_phi)]
        self.chopsticks = [Lock() for _ in range(num_of_chopsticks)]

    def philosopher(self, i):
        while self.meals[i] > 0:
            time.sleep(0.5)
            if not self.chopsticks[i].locked():
                self.chopsticks[i].acquire()
                time.sleep(0.5)
                if not self.chopsticks[i+1].locked():
                    self.chopsticks[i+1].acquire()
                    self.meals[i] -= 1
                    time.sleep(0.5)
                    self.chopsticks[i+1].release()
                self.chopsticks[i].release()


if __name__ == '__main__':
    di = DiningPhilosophess(5, 6)
    th_list = []
    for i in range(5):
        th_list.append(Thread(target=di.philosopher, args=(i,)))
        th_list[i].start()
    line_count = 0
    while sum(di.meals) >= 0:
        line_count += 1
        print("line %d: " % line_count, di.meals)
        time.sleep(1)
        if sum(di.meals) == 0:
            break
    for i in range(4):
        th_list[i].join()





