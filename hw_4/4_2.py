import os
import math
import time
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from functools import partial

log_dir = "artifacts/4_2"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, "logs.txt"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def integrate_segment(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_type="thread"):
    logging.info(f"Запуск integrate с n_jobs={n_jobs}, executor_type={executor_type}")
    
    step = (b - a) / n_jobs
    ranges = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    partial_n_iter = n_iter // n_jobs

    executor_cls = ThreadPoolExecutor if executor_type == "thread" else ProcessPoolExecutor
    with executor_cls(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate_segment, f, start, end, partial_n_iter) for start, end in ranges]
        results = [future.result() for future in futures]

    return sum(results)

def main():
    a, b = 0, math.pi / 2
    n_iter = 10000000
    max_jobs = 2 * os.cpu_count() 
    
    results = []
    for executor_type in ["thread", "process"]:
        for n_jobs in range(1, max_jobs + 1):
            start_time = time.time()
            result = integrate(math.cos, a, b, n_jobs=n_jobs, n_iter=n_iter, executor_type=executor_type)
            elapsed_time = time.time() - start_time
            
            logging.info(f"{executor_type.upper()} | n_jobs={n_jobs}: результат={result}, время={elapsed_time:.2f} сек")
            results.append(f"{executor_type},{n_jobs},{elapsed_time:.2f}")

    output_dir = "artifacts/4_2"
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "results.csv"), "w") as file:
        file.write("Executor Type,Workers,Time\n")
        file.write("\n".join(results))

if __name__ == "__main__":
    main()
