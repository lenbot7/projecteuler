from math import *
from typing import Iterator
def fibonacci_generator() -> Iterator[int]:
    yield 1
    yield 2
    previous = 1
    current = 2
    while True:
        previous, current = current, current + previous
        yield current


def solution_generator() -> int:
    fib_sum = 0
    for fib_i in fibonacci_generator():
        if fib_i % 2 == 0:
            fib_sum += fib_i
        if fib_i > 4_000_000:
            break
    return fib_sum
print(solution_generator())