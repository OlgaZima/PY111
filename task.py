from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы

    return nx.shortest_path_lenght(graph, source=0, target=nx.DiGraph.__len__() - 1, weight='weight')

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = nx.DiGraph()  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней

    stairway_graph.add_weighted_edges_from([
        (0, 1, 5),
        (0, 2, 11),
        (1, 2, 11),
        (1, 3, 43),
        (2, 3, 43),
        (2, 4, 2),
        (3, 4, 2),
        (3, 5, 23),
        (4, 5, 23),
        (4, 6, 43),
        (5, 6, 43),
        (5, 7, 22),
        (6, 7, 22),
        (6, 8, 12),
        (7, 8, 12),
        (7, 9, 6),
        (8, 9, 6),
        (8, 10, 8),
        (9, 10, 8)
    ])

    print(stairway_path(stairway_graph))  # 72
