import ctypes
from math import sqrt
from time import perf_counter

c_lib = ctypes.cdll.LoadLibrary("./prime_count.so")
prime_count_c = c_lib.prime_count
prime_count_c.argtypes = [ctypes.c_float,]

def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0: return False
    return True

def prime_count(x: float) -> int:
    count = 0
    for i in range(2, int(x)):
        if is_prime(i): count += 1
    return count

if __name__ == "__main__":
    n = 1_000_000
    print("Python:")
    start = perf_counter()
    result = prime_count(n)
    end = perf_counter()
    print(f"Prime count of {n}: {result}")
    print(f"Took {end - start} seconds")
    print("--------------------")
    print("C:")
    start = perf_counter()
    result = prime_count_c(n)
    end = perf_counter()
    print(f"Prime count of {n}: {result}")
    print(f"Took {end - start} seconds")