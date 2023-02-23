from typing import Any


class Stack:
    def __init__(self):
        self._stack = []
    # TODO использовать python list для реализации стека</placeholder>

    def push(self, elem: Any) -> None:
        self._stack.append(elem)
         # TODO реализовать операцию push</placeholder>

    def pop(self) -> Any:
        if len(self._stack) == 0:
            raise IndexError()
        return self._stack.pop()
         # TODO реализовать операцию po</placeholder>

    def peek(self, ind: int = 0) -> Any:
        if not isinstance(ind, int):
            raise TypeError()
        if ind < 0 or ind > len(self._stack) - 1:
            raise IndexError()
        return self._stack[(len(self._stack) - 1 - ind)]


        # TODO реализовать операцию peell</placeholder>


    def clear(self) -> None:
        return self._stack.clear()


       # TODO реализовать операцию clear</placeholder>

    def __len__(self) -> int:
        return len(self._stack)

        # TODO реализовать операцию __len__</placeholder>

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.peek(0))



