"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
          # TODO использовать deque для реализации очереди с приоритетами</placeholder>

        self._queue = dict()
        for i in range(self.LOW_PRIORITY + 1):
            self._queue[i] = []

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
         # TODO реализовать метод enqueue</placeholder>

        self._queue[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
         # TODO реализовать метод dequeue</placeholder>
        for i in range(len(self._queue)):
            if len(self._queue[i]) == 0:
                continue
            return self._queue[i].pop(0)
        raise IndexError()


    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        # TODO реализовать метод peek</placeholder>

        if not isinstance(ind, int):
            raise TypeError()
        if not 0 <= ind < len(self._queue[priority]):
            raise IndexError()
        if len(self._queue[priority]) == 0:
            return None
        else:
            return self._queue[priority][ind]

    def clear(self) -> None:
        """ Очистка очереди. """
         # TODO реализовать метод clear</placeholder>
        for key, value in self._queue.items():
            value.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        # TODO реализовать метод __len__</placeholder>
        len_ = 0
        for gueue in self._queue.values():
            len_ += len(gueue)
        return len_


