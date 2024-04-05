def fizz_buzz(n: int) -> str:
    """FizzBuzzを行う

    Args:
        n (int): 数値

    Returns:
        str: FizzBuzzの結果
    """

    def func(n: int) -> str:
        match (n % 3, n % 5):
            case (0, 0):
                return "FizzBuzz"
            case (0, _):
                return "Fizz"
            case (_, 0):
                return "Buzz"
            case _:
                return str(n)

    return func(n)


if __name__ == "__main__":
    for i in range(1, 16):
        print(fizz_buzz(i))
