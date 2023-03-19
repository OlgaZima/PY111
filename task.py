def stairway_path(count_stairs: int) -> int:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до вершины
    """
    ...  # TODO найти количество маршрутов до каждой ступени
    if count_stairs < 0:
        raise ValueError()
    f0 = 1
    f1 = 2
    if count_stairs == 0:
        return f0
    if count_stairs == 1:
        return f1
    for i in range(2, count_stairs + 1):
        f0, f1 = f1, f0 + f1
    return f1


if __name__ == '__main__':
    print(stairway_path(0))  # 1
    print(stairway_path(5))  # 13
