def sum(ints: list[int]) -> int:
    """足し算を行う

    Args:
        ints (list[int]): 数値のリスト

    Returns:
        int: 合計
    """

    def func(ints: list[int]) -> int:
        match ints:
            case []:
                return 0
            case _:
                return ints[0] + sum(ints[1:])

    return func(ints)


if __name__ == "__main__":
    print(sum([1, 2]))
    print(sum([1, 2, 3]))
    print(sum([1, 2, 3, 4]))
