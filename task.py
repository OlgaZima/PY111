from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования
    Table = [[1] * m for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            Table[i][j] = Table[i][j - 1] + Table[i - 1][j] + Table[i - 1][j - 1]
    return Table


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
