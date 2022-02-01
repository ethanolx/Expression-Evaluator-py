# type: ignore
'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from .temp_node import TempNode
from .exceptions import InvalidOptionError
from .print_orientation import PrintOrientation
from .tree_traversal_order import TreeTraversalOrder


# Class for generic trees
class Tree:
    def __init__(self,
                 depth_symbol: str = '.') -> None:
        # Protected properties
        self._root = None
        self._currentPointer = None

        # Private properties
        self.__depth_symbol = depth_symbol
        self.__print_orientation: PrintOrientation = PrintOrientation.HORIZONTAL
        self.__print_traversal_order: TreeTraversalOrder = TreeTraversalOrder.IN_ORDER

    # Getter for print orientation
    @property
    def print_orientation(self):
        return self.__print_orientation

    # Setter for print orientation
    @print_orientation.setter
    def print_orientation(self, new_print_orientation: str):
        if new_print_orientation == '':
            return
        if new_print_orientation not in 'hv':
            raise InvalidOptionError(f'Unknown option \'{new_print_orientation}\' encountered for print_mode (expected \'h\' or \'v\')')
        available_print_modes = {
            'h': PrintOrientation.HORIZONTAL,
            'v': PrintOrientation.VERTICAL
        }
        self.__print_orientation = available_print_modes[new_print_orientation]

    # Getter for print traversal order
    @property
    def print_traversal_order(self):
        return self.__print_traversal_order

    # Setter for print traversal order
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

    # Prints the available options for tree traversal orders
    @staticmethod
    def __print_traversal_menu():
        print()
        print("Please select how you want to traverse the tree [a/b/c]:\n"
              "\ta. Inorder (R, N, L)\n"
              "\tb. Preorder (N, R, L)\n"
              "\tc. Postorder (R, L, N)\n")

    # Print methods
    # DFS
    def __print_inorder(self):
        def __internal_recursive(node, depth: int = 0):
            if node is not None:
                __internal_recursive(node=node._right, depth=depth + 1)
                print(self.__depth_symbol * depth + str(node))
                __internal_recursive(node=node._left, depth=depth + 1)
        __internal_recursive(node=self._root, depth=0)

    def __print_preorder(self):
        def __internal_recursive(node, depth: int = 0):
            if node is not None:
                print(self.__depth_symbol * depth + str(node))
                __internal_recursive(node=node._right, depth=depth + 1)
                __internal_recursive(node=node._left, depth=depth + 1)
        __internal_recursive(node=self._root, depth=0)

    def __print_postorder(self):
        def __internal_recursive(node, depth: int = 0):
            if node is not None:
                __internal_recursive(node=node._right, depth=depth + 1)
                __internal_recursive(node=node._left, depth=depth + 1)
                print(self.__depth_symbol * depth + str(node))
        __internal_recursive(node=self._root, depth=0)

    # BFS
    def __print_vertical(self):
        self._root.update_widths()
        current_nodes = [self._root]
        next_nodes = []

        # Continue while there is at least one non-temporary node left
        while any(map(lambda n: not isinstance(n, TempNode), current_nodes)):
            print(len(current_nodes))
            for n in current_nodes:
                print(n.display(), end=' ')
                if n._left is None and n._right is None:
                    next_nodes.append(TempNode(width=n._width))
                else:
                    if n._left is not None:
                        next_nodes.append(n._left)
                    if n._right is not None:
                        next_nodes.append(n._right)

            current_nodes = next_nodes
            next_nodes = []
            print()

    # Options 1 & 2 - Public method for printing the tree
    #   - Uses __print_orientation and __print_traversal_order to determine how to print the tree
    def print_tree(self):
        if self.__print_orientation is PrintOrientation.VERTICAL:
            self.__print_vertical()
        else:
            if self.__print_traversal_order is TreeTraversalOrder.PRE_ORDER:
                self.__print_preorder()
            elif self.__print_traversal_order is TreeTraversalOrder.IN_ORDER:
                self.__print_inorder()
            else:
                self.__print_postorder()

    # Resets the pointers
    def reset(self):
        self._root = None
        self._currentPointer = None

    # Oprion 5 - Interface for users to change the print orientation and/or traversal order
    def change_print_mode(self):
        new_print_orientation = input('Enter new print mode (h/v): ').strip().lower()

        self.print_orientation = new_print_orientation

        if new_print_orientation == 'h':
            self.__print_traversal_menu()
            new_traversal_order = input('Enter new print mode (a/b/c): ').strip().lower()
            self.print_traversal_order = new_traversal_order

        print()
        print("Printing Mode Updated")
        print("Orientation:\t{}".format(self.print_orientation.value).expandtabs(6))
        print("Traversal Order:\t{}".format(self.print_traversal_order.value).expandtabs(6))
