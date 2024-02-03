import random
import time
from threading import Thread, Lock, Semaphore


class DiningPhilosophess:
    def __init__(self, num_of_phi, num_of_chopsticks):
        self.num_of_phi = num_of_phi
        self.num_of_chopsticks = num_of_chopsticks
        self.meals = [7 for _ in range(num_of_phi)]
        # 代表信号量一时间只能够被1个线程使用
        self.chopsticks = [Semaphore(2) for _ in range(num_of_chopsticks)]
        self.phi_status = ["  _  " for _ in range(self.num_of_phi)]
        self.chopsticks_status = ["     " for _ in range(self.num_of_chopsticks)]

    def philosopher(self, i):
        j = (i + 1) % (self.num_of_chopsticks - 1)
        while self.meals[i] > 0:
            self.phi_status[i] = "  T  "
            time.sleep(0.5)
            self.phi_status[i] = "  _  "
            # Phi acquire the left chopstick
            if self.chopsticks[i].acquire(timeout=0.5):
                self.chopsticks_status[i] = " |   "
                # Phi acquire the right chopsticks
                if self.chopsticks[j].acquire(timeout=0.5):
                    self.chopsticks_status[i] = " | | "
                    self.meals[i] -= 1
                    self.phi_status[i] = "  E  "
                    time.sleep(random.uniform(0, 1))
                    self.chopsticks[j].release()
                    self.phi_status[i] = "  _  "
                    self.chopsticks_status[i] = " |   "
                self.chopsticks[i].release()
                self.chopsticks_status[i] = "     "


if __name__ == '__main__':
    di = DiningPhilosophess(5, 5)
    th_list = []
    for i in range(5):
        th_list.append(Thread(target=di.philosopher, args=(i,)))
        th_list[i].start()
    line_count = 0
    while sum(di.meals) >= 0:
        line_count += 1
        print("=" * di.num_of_phi * 5)
        print("line %d: " % line_count, di.meals)
        print("".join(di.phi_status))
        print("".join(di.chopsticks_status))
        print("  " + "    ".join(map(str, di.meals)))
        print("=" * di.num_of_phi * 5)
        time.sleep(1)
        if sum(di.meals) == 0:
            break
    for i in range(4):
        th_list[i].join()




