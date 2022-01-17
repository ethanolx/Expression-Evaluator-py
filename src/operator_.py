from .math_node import MathNode


class Operator(MathNode):
    def __init__(self, symbol, func, priority) -> None:
        super().__init__(None, symbol, func)
        self._priority = priority

    def __lt__(self, otherNode) -> bool:
        return self._priority < otherNode._priority

    def __gt__(self, otherNode) -> bool:
        return self._priority > otherNode._priority

    def copy(self) -> 'Operator':
        return Operator(symbol=self._symbol, func=self._func, priority=self._priority)