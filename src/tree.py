from typing import List, Literal, Optional

from .math_node import MathNode
from .temp_node import TempNode
from .exceptions import InvalidOptionError
from .node import Node
from .print_mode import PrintMode
from .tree_traversal_order import TreeTraversalOrder


class Tree:
    def __init__(self,
                 depth_symbol: str = '.') -> None:
        self._root: Optional[Node] = None
        self._currentPointer: Optional[Node] = None
        self.__depth_symbol = depth_symbol
        self.__print_mode: PrintMode = PrintMode.HORIZONTAL
        self.__print_traversal_order: TreeTraversalOrder = TreeTraversalOrder.IN_ORDER

    @property
    def print_mode(self):
        return self.__print_mode

    @print_mode.setter
    def print_mode(self, new_print_mode: str):
        if new_print_mode == '':
            return
        if new_print_mode not in 'hv':
            raise InvalidOptionError(f'Unknown option \'{new_print_mode}\' encountered for print_mode (expected \'h\' or \'v\')')
        available_print_modes = {
            'h': PrintMode.HORIZONTAL,
            'v': PrintMode.VERTICAL
        }
        self.__print_mode = available_print_modes[new_print_mode]

    @property
    def print_traversal_order(self):
        return self.__print_traversal_order

    @print_traversal_order.setter
    def print_traversal_order(self, new_traversal_order: str):
        if new_traversal_order == '':
            return
        if new_traversal_order not in 'abc':
            raise InvalidOptionError(f'Unknown option \'{new_traversal_order}\' encountered for traversal_order (expected a, b or c)')
        possible_traversal_orders = {
            'a': TreeTraversalOrder.IN_ORDER,
            'b': TreeTraversalOrder.PRE_ORDER,
            'c': TreeTraversalOrder.POST_ORDER
        }
        self.__print_traversal_order = possible_traversal_orders[new_traversal_order]

    def __print_inorder(self):
        def __internal_recursive(node: Optional[Node], depth: int = 0):
            if node is not None:
                __internal_recursive(node=node._right, depth=depth + 1)
                print(self.__depth_symbol * depth + str(node))
                __internal_recursive(node=node._left, depth=depth + 1)
        __internal_recursive(node=self._root, depth=0)

    def __print_preorder(self):
        def __internal_recursive(node: Optional[Node], depth: int = 0):
            if node is not None:
                print(self.__depth_symbol * depth + str(node))
                __internal_recursive(node=node._right, depth=depth + 1)
                __internal_recursive(node=node._left, depth=depth + 1)
        __internal_recursive(node=self._root, depth=0)

    def __print_postorder(self):
        def __internal_recursive(node: Optional[Node], depth: int = 0):
            if node is not None:
                __internal_recursive(node=node._right, depth=depth + 1)
                __internal_recursive(node=node._left, depth=depth + 1)
                print(self.__depth_symbol * depth + str(node))
        __internal_recursive(node=self._root, depth=0)

    def __print_vertical(self):
        self._root.update_widths()
        current_nodes: List[Node] = [self._root]
        next_nodes = []
        while list(filter(lambda n: isinstance(n, MathNode), current_nodes)):
            for n in current_nodes:
                print(n.display(), end=' ')
                if n._left is None and n._right is None:
                    next_nodes.append(TempNode(width=n._width))
                else:
                    next_nodes.append(n._left)
                    next_nodes.append(n._right)

            current_nodes = next_nodes
            next_nodes = []
            print()

    def print_tree(self):
        if self.__print_mode is PrintMode.VERTICAL:
            self.__print_vertical()
        else:
            if self.__print_traversal_order is TreeTraversalOrder.PRE_ORDER:
                self.__print_preorder()
            elif self.__print_traversal_order is TreeTraversalOrder.IN_ORDER:
                self.__print_inorder()
            else:
                self.__print_postorder()

    def reset(self):
        self._root = None
        self._currentPointer = None

    def change_print_mode(self):
        new_print_mode = input('Enter new print mode (h/v): ').strip().lower()

        self.print_mode = new_print_mode

        if new_print_mode == 'h':
            self.print_traversal_menu()
            new_traversal_order = input('Enter new print mode (a/b/c): ').strip()
            self.print_traversal_order = new_traversal_order

        print()
        print("Printing Mode Updated")
        print("Orientation:\t{}".format(self.print_mode.value).expandtabs(6))
        print("Traversal Order:\t{}".format(self.print_traversal_order.value).expandtabs(6))

    @staticmethod
    def print_traversal_menu():
        print()
        print("Please select how you want to traverse the Parse Tree [a/b/c/d]:\n"
            "\ta. Inorder (Left, Root, Right)\n"
            "\tb. Preorder (Root, Left, Right)\n"
            "\tc. Postorder (Left, Right, Root)\n")