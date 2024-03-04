import sys
sys.path.append('../')
from cloudburst.client.client import CloudburstConnection
import multiprocessing
import os
import time

# 定义一个函数，用于在进程中执行的任务
def worker(process_id):
    local_cloud = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
    func = local_cloud.register(lambda _, x : x + 100, 'add')
    print(f"Worker {process_id} started in process {os.getpid()}")
    # time.sleep(3 * process_id)  # 模拟任务执行
    print(f"process {process_id} result = {func(100).get()}")
    print(f"Worker {process_id} finished in process {os.getpid()}")

if __name__ == "__main__":
    # 创建多个进程
    num_processes = 2
    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()

    print("All processes have finished")
