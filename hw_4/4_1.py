import os
import time
import threading
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def run_sync(n, count):
    for _ in range(count):
        fibonacci(n)

def run_threads(n, count):
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def run_processes(n, count):
    processes = []
    for _ in range(count):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

def main():
    n = 40
    count = 10
    
    results = []
    
    start = time.time()
    run_sync(n, count)
    sync_time = time.time() - start
    results.append(f"Синхронный запуск: {sync_time:.2f} секунд")
    
    start = time.time()
    run_threads(n, count)
    threads_time = time.time() - start
    results.append(f"Потоки: {threads_time:.2f} секунд")
    
    start = time.time()
    run_processes(n, count)
    processes_time = time.time() - start
    results.append(f"Процессы: {processes_time:.2f} секунд")
    
    output_dir = "artifacts/4_1"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "results.txt"), "w") as file:
        file.write("\n".join(results))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
