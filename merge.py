from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
     # TODO реализуйте сортировку слиянием
    if len(container) <= 1:
        return container
    mean_ = len(container) // 2
    left = sort(container[:mean_])
    right = sort(container[mean_:])
    return merge(left, right)


def merge(a, c: List[int]) -> List[int]:
    container = []
    i = j = 0
    while i < len(a) and j < len(c):
        if a[i] < c[j]:
            container.append(a[i])
            i += 1
        else:
            container.append(c[j])
            j += 1
    if i < len(a):
        container += a[i:]
    elif j < len(c):
        container += c[j:]
    return container

# print(sort([1, 0, 5, 6, 6, 6, 8, 2]))


