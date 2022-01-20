from abc import ABC, abstractmethod
from typing import Any


class Node(ABC):
    def __init__(self,
                 value,
                 width) -> None:
        self._value = value
        self._parent = None
        self._left = None
        self._right = None
        self._width = width

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return self.__str__()

    def display(self):
        if self._left is not None and self._right is not None:
            diff = self._right._width - self._left._width
            return ' ' * abs(min(diff, 0)) + f'{self.__str__():^{self._width - abs(diff)}}' + ' ' * max(diff, 0)
        return self.__str__()

    def update_widths(self):
        if self._left is not None:
            self._left.update_widths()
        if self._right is not None:
            self._right.update_widths()
        if self._left is not None and self._right is not None:
            self._width = self._left._width + 1 + self._right._width