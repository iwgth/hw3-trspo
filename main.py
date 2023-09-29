import threading
import time
from queue import Queue
#12ma
def collatz(n, results):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    results.put(count)

def main():
    n = int(input("Введіть N: "))
    numbers = list(range(1, n + 1))
    threads_count = int(input("Введіть кількість потоків: "))
    results = Queue()
    threads = []

    def worker():
        while True:
            try:
                number = numbers.pop()
            except IndexError:
                break
            collatz(number, results)

    for _ in range(threads_count):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    steps_sum = 0
    while not results.empty():
        steps_sum += results.get()

    average_steps = steps_sum / n
    print("Середня кількість кроків:", average_steps)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Час виконання:", end_time - start_time)
