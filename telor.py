from typing import Union
from itertools import count
import math


DELTA = 0.000001


def factorial_iterative(n: int) -> int:
    fact = 1
    for i in range(1, n + 1):
        if n == 0:
            return fact
        else:
            fact *= i
    return fact


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    x_ = x
    one = - 1
    sum_ = 0
    if 0 <= x <= 2 * math.pi:
        for i in count():
            x_ = x ** (2 * i + 1)
            one_ = one ** i
            fact = factorial_iterative(2 * i + 1)
            sum__ = one_ * x_ / fact
            sum_ += sum__
            if abs(sum__) <= DELTA:
                return sum_





     # TODO вычислить sin(x) с помощью разложения сумму бесконечного ряда
# print(sinx(1.55433))
# print(math.sin(1.55433))