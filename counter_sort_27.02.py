from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
     # TODO реализовать алгоритм сортировки подсчетами

    if len(container) == 0:
        return container
    max_ = max(container)
    histogram = [0 for i in range(max_ + 1)]

    for i in container:
        histogram[i] += 1
    for j in range(1, len(histogram)):
        histogram[j] += histogram[j - 1]  #for index in the sorted list

    container_sort = [0] * len(container)
    for ii in range(len(container)):
        container_sort[histogram[container[ii]] - 1] = container[ii]
        histogram[container[ii]] -= 1

    return container_sort

    # for i, val in enumerate(histogram):
    #     for j in range(val):
    #         container_sort.append(i)
    # for i in range(len(histogram)):
    #     container_sort += histogram[i] * [i]


if __name__ == "__main__":
    container = [1, 0, 1, 5, 4, 4, 3, 2, 1]
    print(sort(container))
    print([])
    print([1])

