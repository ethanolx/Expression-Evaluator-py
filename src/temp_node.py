from .node import Node


class TempNode(Node):
    def __init__(self, width) -> None:
        super().__init__(value=None, width=width)

    def display(self):
        return ' ' * self._width