from functools import lru_cache


@lru_cache()
def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    ...  # TODO реализовать рекурсивный алгоритм

    # if not isinstance(n, int):
    #     raise TypeError()
    if n < 0:
        raise ValueError()
    if n in (1, 2):
        return 1
    elif n == 0:
        return 0
    return fib_recursive(n-1) + fib_recursive(n-2)


if __name__ == '__main__':
    print(fib_recursive(2))  # 1
    print(fib_recursive(15))  # 610
