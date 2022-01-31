'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from .math_node import MathNode


class Operator(MathNode):
    def __init__(self, symbol, func, priority) -> None:
        super().__init__(None, symbol, func)
        self.__priority = priority

    # Operators are compared based on their priority
    def __lt__(self, otherNode) -> bool:
        return self.__priority < otherNode.get_priority()

    def __gt__(self, otherNode) -> bool:
        return self.__priority > otherNode.get_priority()

    # Getter for priority
    def get_priority(self) -> int:
        return self.__priority

    # Increase the priority of the root of an expression within parentheses
    def augment_priority(self):
        self.__priority += 3

    # Returns a copy of self
    def copy(self) -> 'Operator':
        return Operator(symbol=self._symbol, func=self._func, priority=self.__priority)
