"""サンプルモジュール"""

from typing import Generator

from sum import sum


def fib(n: int) -> Generator[int, None, None]:
    """フィボナッチ数列を生成するジェネレータ"""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def greeting(name: str) -> str:
    """挨拶を返す

    Args:
        name (str): 名前

    Returns:
        str: "Hello " + name
    """
    return "Hello " + name


if __name__ == "__main__":
    print("Hello World!")
    print(sum(1, 2))
    print(list(fib(10)))
