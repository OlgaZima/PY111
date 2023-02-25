from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
     # TODO реализовать алгоритм бинарного поиска

    if right_border is None:
        right_border = len(seq) - 1

    if left_border <= right_border:
        mid = left_border + (right_border - left_border) // 2
        if seq[mid] == value:
            if not 0 <= mid - 1 < len(seq) or seq[mid - 1] != value:
                return mid
            return binary_search(value, seq, left_border, right_border=mid-1)
            # while True:
            #     if seq[mid - 1] == value and 0 < mid - 1 < len(seq):
            #         mid -= 1
            #     else:
            #         break
            # return mid
        elif seq[mid] < value:
            left_border = mid + 1
            return binary_search(value, seq, left_border, right_border)
        else:
            right_border = mid - 1
            return binary_search(value, seq, left_border, right_border)
    raise ValueError()


print(binary_search(3, [1, 1, 2, 3, 3, 3, 29]))