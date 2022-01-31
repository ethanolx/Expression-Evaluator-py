'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from .math_node import MathNode
from .exceptions import InvalidExpressionError


# Class for operands (numbers)
class Operand(MathNode):
    def __init__(self, value) -> None:
        super().__init__(value, value, lambda _, __: self._value)

    # Operands have the highest priority
    def __lt__(self, _) -> bool:
        return False

    def __gt__(self, _) -> bool:
        return True

    # Method should not be called if expression is valid
    def get_priority(self):
        raise InvalidExpressionError()

    # Increase the priority of the root of an expression within parentheses
    def augment_priority(self):
        pass

    # Returns a copy of self
    def copy(self) -> 'Operand':
        return Operand(value=self._value)