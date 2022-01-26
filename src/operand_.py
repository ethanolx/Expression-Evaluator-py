'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from src.exceptions import InvalidExpressionError
from .math_node import MathNode


class Operand(MathNode):
    def __init__(self, value) -> None:
        super().__init__(value, value, lambda _, __: self._value)

    def __lt__(self, _) -> bool:
        return False

    def __gt__(self, _) -> bool:
        return True

    def get_priority(self):
        raise InvalidExpressionError('Invalid Expression')

    def augment_priority(self):
        pass

    def copy(self) -> 'Operand':
        return Operand(value=self._value)