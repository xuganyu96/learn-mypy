from __future__ import annotations
from typing import Iterator

def fib(n: int) -> Iterator[int]:
    prev = 0
    cur = 1

    for _ in range(n):
        yield cur
        prev, cur = cur, cur + prev


if __name__ == "__main__":
    for num in fib(64):
        print(num)

