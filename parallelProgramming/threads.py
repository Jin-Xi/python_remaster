import threading
import time

def worker(thread_name, delay):
    print(f"{thread_name} is starting...")
    time.sleep(delay)
    print(f"{thread_name} is done.")

# 创建两个线程
thread_A = threading.Thread(target=worker, args=("Thread A", 2))
thread_B = threading.Thread(target=worker, args=("Thread B", 4))

# 启动两个线程
thread_A.start()
thread_B.start()

# 在主线程中分别等待两个线程完成
thread_A.join()
print("threads A starts")
thread_B.join()

print("Main thread is done.")
