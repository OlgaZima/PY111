def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
   # TODO реализовать рекурсивный алгоритм нахождения факториала
    if isinstance(n, int) and n >= 0:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial_recursive(n-1)
    if not isinstance(n, int):
        raise TypeError()
    else:
        raise ValueError()
