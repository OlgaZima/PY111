from typing import Any


class Queue:
    def __init__(self):
        self._list_ = []  # TODO инициализировать список
        """
        [0] - начало очереди, [-1] - конец очерди   """

    def enqueue(self, elem: Any) -> None:  #O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._list_.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:     #O(1)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        # try:
        #     return self._list_.pop(0)
        # except IndexError as e:
        #     return e
        if len(self._list_) == 0:
            raise IndexError()
        else:
            return self._list_.pop(0)
         # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:      #O(N)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
                     """
        for i in range(len(self._list_)):
            if not isinstance(ind, int):
                raise TypeError("Указан не целочисленный тип индекса")

            if ind >= len(self._list_) or ind < 0:
                raise IndexError("Индекс вне границ очереди")

            elif i == ind:
                return self._list_[i]
                         #TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        return self._list_.clear()  # TODO реализовать метод clear

    def __len__(self):         #O(1)
        """ Количество элементов в очереди. """
        return len(self._list_) # TODO реализовать метод __len__


# if __name__ == "__main__":
#     a = Queue()
#     a.enqueue(1)
#     a.enqueue(2)
#     a.enqueue(3)
#     print("Удаление элемента из начала очереди:", a.dequeue())
#     print("Посмотреть 1-ый элемент:", a.peek())
#     print("Посмотреть любой элемент:", a.peek(1))
#     print("Очистить очередь:", a.clear())



