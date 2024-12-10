import time
import string
import multiprocessing
from multiprocessing import Queue, Process
import sys
from multiprocessing.queues import Empty

def rot13(text: str) -> str:
    return text.translate(str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    ))

def print_with_timestamp(msg: str):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"{timestamp} - {msg}")

def process_a(queue_in: Queue, queue_out: Queue, stop_event: multiprocessing.Event):
    while not stop_event.is_set():
        msg = queue_in.get()
        if msg == "exit":
            break
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        lower_msg = msg.lower()
        print_with_timestamp(f"Процесс A преобразовал сообщение: {lower_msg}")
        queue_out.put((timestamp, lower_msg))

def process_b(queue_in: Queue, queue_out: Queue, stop_event: multiprocessing.Event):
    while not stop_event.is_set():
        msg = queue_in.get()
        if msg == "exit":
            break
        timestamp, original_msg = msg
        encoded_msg = rot13(original_msg)
        print_with_timestamp(f"Закодированное сообщение: {encoded_msg}")
        queue_out.put((timestamp, encoded_msg))
        time.sleep(5)

def process_results(queue_result: Queue):
    while True:
        try:
            result = queue_result.get(timeout=5)
            timestamp, encoded_msg = result
            print_with_timestamp(f"Получено от процесса B: {encoded_msg}")
        except Empty:
            continue

def main():
    queue_a = Queue()
    queue_b = Queue()
    queue_result = Queue()
    stop_event = multiprocessing.Event()

    process_a_instance = Process(target=process_a, args=(queue_a, queue_b, stop_event))
    process_b_instance = Process(target=process_b, args=(queue_b, queue_result, stop_event))

    process_a_instance.start()
    process_b_instance.start()

    result_handler = Process(target=process_results, args=(queue_result,))
    result_handler.start()

    print("Введите сообщения для отправки в процесс A:")
    while True:
        msg = sys.stdin.readline().strip()
        if msg == 'exit':
            break
        print_with_timestamp(f"Сообщение отправлено в процесс A: {msg}")
        queue_a.put(msg)

    stop_event.set()
    process_a_instance.join()
    process_b_instance.join()
    result_handler.terminate()

if __name__ == "__main__":
    main()
