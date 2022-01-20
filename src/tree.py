from typing import Any, Callable, Optional

from .exceptions import InvalidOptionError
from .node import Node
from enum import Enum


class TreeTraversalOrder(Enum):
    PRE_ORDER = 0
    IN_ORDER = 1
    POST_ORDER = 2


class Tree:
    def __init__(self,
                 depth_symbol: str = '.') -> None:
        self.root: Optional[Node] = None
        self.currentPointer: Optional[Node] = None
        self.__depth_symbol = depth_symbol
        self.__print_mode = 'h'
        self.__print_traversal_order: TreeTraversalOrder = TreeTraversalOrder.IN_ORDER

    def print_inorder(self):
        def __internal_recursive(node: Optional[Node], depth: int = 0):
            if node is not None:
                __internal_recursive(node=node.right, depth=depth + 1)
                print(self.__depth_symbol * depth + str(node))
                __internal_recursive(node=node.left, depth=depth + 1)

    def reset(self):
        self.root = None
        self.currentPointer = None

    def print_vertical(self) -> str:
        self.root.update_widths()
        current_nodes = [self.root]
        next_nodes = []
        representation = []
        while list(filter(lambda n: isinstance(n, Node), current_nodes)):
            row = []
            for n in current_nodes:
                if isinstance(n, Node):
                    row.append(n.padded_display())
                    if n.left is None and n.right is None:
                        next_nodes.append(n.get_width())
                    else:
                        next_nodes.append(n.left)
                        next_nodes.append(n.right)
                else:
                    row.append(' ' * n)
                    next_nodes.append(n)

            current_nodes = next_nodes
            next_nodes = []
            representation.append(' '.join(row))
        return '\n'.join(representation)

