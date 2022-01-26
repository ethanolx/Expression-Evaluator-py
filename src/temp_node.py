'''
   Class: DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from .node import Node


class TempNode(Node):
    def __init__(self, width) -> None:
        super().__init__(value=None, width=width)

    def display(self):
        return ' ' * self._width