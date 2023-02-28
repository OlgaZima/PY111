from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
     # TODO реализовать алгоритм быстрой сортировки
    if len(container) <= 1:
        return container
    elem_opor = container[len(container) // 2]
    left = list(filter(lambda x: x < elem_opor, container))
    mean_ = [x for x in container if x == elem_opor]
    right = list(filter(lambda x: x > elem_opor, container))
    return sort(left) + mean_ + sort(right)


# print(sort([1, 0, 5, 6, 6, 6, 8, 2]))