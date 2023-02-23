def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # TODO реализовать итеративный алгоритм нахождения факториала</placeholder>
    if isinstance(n, int) and n >= 0:
        fact = 1
        for i in range(1, n + 1):
            if n == 0:
                return fact
            else:
                fact *= i
        return fact
    elif not isinstance(n, int):
        raise TypeError()
    else:
        raise ValueError
# print(factorial_iterative(2))