from typing import Any
from .node import Node


class MathNode(Node):
    def __init__(self, value, symbol, func) -> None:
        super().__init__(value)
        self._symbol = symbol
        self._func = func

    def __call__(self) -> Any:
        if self.left is not None:
            self.left()
        if self.right is not None:
            self.right()
        self._value = self._func(self.left, self.right)

    def __str__(self) -> str:
        return str(self._symbol)