from typing import Generator


def sum(a: int, b: int) -> int:
    return a + b


def fib(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b


def greeting(name: str) -> str:
    return 'Hello ' + name


if __name__ == "__main__":
    print("Hello World!")
    print(sum(1, 2))
