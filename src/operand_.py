from .math_node import MathNode


class Operand(MathNode):
    def __init__(self, value) -> None:
        super().__init__(value, value, lambda _, __: self._value)

    def __lt__(self, otherNode) -> bool:
        return False

    def __gt__(self, otherNode) -> bool:
        return True

    def copy(self) -> 'Operand':
        return Operand(value=self._value)