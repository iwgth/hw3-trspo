import multiprocessing
import time
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
def calculate_average_steps(numbers, num_threads):
    pool = multiprocessing.Pool(processes=num_threads)
    results = pool.map(collatz_steps, numbers)
    pool.close()
    pool.join()
    return sum(results) / len(numbers)
if __name__ == "__main__":
    N = int(input("Введіть к-ть натуральних чисел: "))
    num_threads = int(input("Введіть к-ть потоків: "))
    numbers = list(range(1, N + 1))
    start_time = time.time()
    average_steps = calculate_average_steps(numbers, num_threads)
    end_time = time.time()
    print(f"Середня к-ть кроків: {average_steps}")
    print(f"Час виконання: {end_time - start_time} с")
    
#Never gonna give you up
#Never gonna let you down
#Never gonna run around and desert you
#Never gonna make you cry
#Never gonna say goodbye
#Never gonna tell a lie and hurt you
