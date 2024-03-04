import sys
sys.path.append('../')
from cloudburst.client.client import CloudburstConnection
import threading
import time

def add(_, x):
    return x + 1

local_cloud = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
func1 = local_cloud.register(lambda _, x: x * x, 'square')
func2 = local_cloud.register(add, 'add')

func = [func1, func2]

# 定义一个任务函数，将在每个线程中执行
def task(thread_id):
    print(f"Thread {thread_id} started and "
        f"exec result: {func[0](thread_id).get()}")
    print(f"Thread {thread_id} finished")

def main():
    # 创建多个线程
    num_threads = 3
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=task, args=(i,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("All threads have finished")

if __name__ == "__main__":
    main()