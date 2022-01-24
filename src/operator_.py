from .math_node import MathNode


class Operator(MathNode):
    def __init__(self, symbol, func, priority) -> None:
        super().__init__(None, symbol, func)
        self.__priority = priority

    def __lt__(self, otherNode) -> bool:
        return self.__priority < otherNode.get_priority()

    def __gt__(self, otherNode) -> bool:
        return self.__priority > otherNode.get_priority()

    def copy(self) -> 'Operator':
        return Operator(symbol=self._symbol, func=self._func, priority=self.__priority)

    def get_priority(self) -> int:
        return self.__priority

    def augment_priority(self):
        self.__priority += 3