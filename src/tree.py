# type: ignore
from typing import Any, Callable, Optional
from .node import Node


class Tree:
    def __init__(self,
                 depth_symbol: str = '.') -> None:
        self.root: Optional[Node] = None
        self.currentPointer: Optional[Node] = None
        self.__depth_symbol = depth_symbol

    def dfs_in(self, node: Node, func: Callable, depth: int = 0):
        if node is not None:
            yield from self.dfs_in(node.right, func=func, depth=depth + 1)
            yield func(node, depth)
            yield from self.dfs_in(node.left, func=func, depth=depth + 1)

    def __str__(self) -> str:
        representation = []
        for s in self.dfs_in(node=self.root, func=lambda n, d: self.__depth_symbol * d + str(n)):
            representation.append(s)
        return '\n'.join(representation)

    def __call__(self) -> Any:
        if self.root is not None:
            self.root()
            return self.root._value
        return None

    def reset(self):
        self.root = None
        self.currentPointer = None