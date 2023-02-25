def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначчи. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    # TODO написать итеративный алгоритм чисел Фибоначчи

    if n < 0:
        raise ValueError()
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1


if __name__ == '__main__':
    print(fib_iterative(2))  # 1
    print(fib_iterative(5))  # 5
