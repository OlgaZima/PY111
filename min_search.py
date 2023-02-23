"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # TODO реализовать итеративный линейный поиск</placeholder>

    if len(arr) == 0:
        raise ValueError()
    else:
        min_ = arr[0]
        ind = 0
        for i, val in enumerate(arr):
            if not isinstance(val, int):
                raise TypeError()
            else:
                if val < min_:
                    min_ = val
                    ind = i
    return ind

# arr = [1, 8, 1, 1]
# print(min_search(arr))
