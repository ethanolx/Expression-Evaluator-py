'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from typing import Any
from .node import Node
from abc import abstractmethod


class MathNode(Node):
    def __init__(self, value, symbol, func) -> None:
        super().__init__(value=value, width=len(str(value)))
        self._symbol = symbol
        self._func = func

    def __call__(self) -> Any:
        if self._left is not None and self._right is not None:
            self._left()
            self._right()
            self._value = self._func(self._left._value, self._right._value)

    def __str__(self) -> str:
        return str(self._symbol)

    @abstractmethod
    def __lt__(self, otherNode) -> bool:
        pass

    @abstractmethod
    def __gt__(self, otherNode) -> bool:
        pass