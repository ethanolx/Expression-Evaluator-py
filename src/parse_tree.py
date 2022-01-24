from typing import List, Literal

from .exceptions import InvalidExpressionError, InvalidOptionError
from .math_node import MathNode
from .operator_ import Operator
from .operand_ import Operand
from .tokenizer import Tokenizer
from .lexer import Lexer
from .tree import Tree


class ParseTree(Tree):
    def __init__(self,
                 depth_symbol: str = '.',
                 mode: int = 1) -> None:
        super().__init__(depth_symbol=depth_symbol)
        self.__token_lookup = [None, {
            '+': Operator('+', lambda a, b: a + b, priority=1),
            '-': Operator('-', lambda a, b: a - b, priority=1),
            '*': Operator('*', lambda a, b: a * b, priority=2),
            '/': Operator('/', lambda a, b: a / b, priority=2),
            '**': Operator('**', lambda a, b: a ** b, priority=3)
        }, {
            '+': Operator('+', lambda a, b: max(a, b), priority=1),
            '-': Operator('-', lambda a, b: min(a, b), priority=1),
            '*': Operator('*', lambda a, b: round(a * b), priority=2),
            '/': Operator('/', lambda a, b: round(a / b), priority=2),
            '**': Operator('**', lambda a, b: a % b, priority=3)
        }][mode]
        self.__tokenizer = Tokenizer(self.__token_lookup.keys())
        self.__lexer = Lexer(self.__token_lookup)
        self.__expression = ''
        self.__prev_build = ''

    def register_new_operator(self):
        print('Here is a simple wizard that will guide you through registering a custom operator...')
        symbol = input('Select a symbol besides [{}, ., (, )] with max length of 3: '.format(', '.join(self.__token_lookup.keys()))).strip()
        if symbol in '.()' or symbol in self.__token_lookup.keys():
            raise InvalidOptionError(f'Illegal symbol encountered: {symbol}')
        if len(symbol) > 3:
            raise InvalidOptionError(f'Symbol {symbol} is too long (max 3)')
        func = eval('lambda a, b: ' + input('Enter function (in Python format) (parameters are a and b): '))
        print('Enter the priority of your operator')
        print('\t1: {+, -} [Default]'.expandtabs(4))
        print('\t2: {*, /}'.expandtabs(4))
        print('\t3: {**}'.expandtabs(4))
        priority_str = input('Operator Priority: ').strip()
        priority = int(priority_str) if priority_str != '' else 1
        if priority not in {1, 2, 3}:
            raise SyntaxError('Invalid priority (expected 1, 2 or 3)')
        new_operator = Operator(symbol=symbol, func=func, priority=priority)
        self.__token_lookup[symbol] = new_operator
        print(f'Successfully registered new operator {repr(new_operator)}')

    def parse(self, token_objs: List[MathNode], i: int = 0):
        while i < len(token_objs):
            n = token_objs[i]
            if n == '(':
                i += 1
                sub_tree, i = ParseTree().parse(token_objs=token_objs, i=i)
                if sub_tree._root is None:
                    raise InvalidExpressionError('Empty parentheses encountered')
                sub_tree._root.augment_priority()
                self.insert(sub_tree._root)
            elif n == ')':
                return self, i
            else:
                self.insert(n)
            i += 1
        return self, i

    def insert(self, node: MathNode):
        if self._root is None:
            self.assign_root(node=node)
        elif self.currentPointer._left is None:
            self.currentPointer = self.assign_child(parent=node, child=self.currentPointer, pos='left')
            self._root = self.currentPointer
        elif self.currentPointer._right is None:
            self.currentPointer = self.assign_child(parent=self.currentPointer, child=node, pos='right')
        else:
            self.currentPointer = self.float_child(currentPointer=self.currentPointer, node=node)

    def assign_root(self, node: MathNode) -> 'ParseTree':
        self._root = node
        self.currentPointer = node
        return self

    def assign_child(self, parent: MathNode, child: MathNode, pos: Literal['left', 'right']) -> 'MathNode':
        child._parent = parent
        if pos == 'left':
            parent._left = child
            return parent
        elif pos == 'right':
            if parent._right is not None:
                child._left = parent._right
            parent._right = child
            return parent if child._left is None else child
        raise ValueError('Pos')

    def float_child(self, currentPointer: MathNode, node: MathNode) -> 'MathNode':
        if currentPointer is None:
            self._root = self.assign_child(parent=node, child=self._root, pos='left')
            return self._root
        if node > currentPointer:
            return self.assign_child(parent=currentPointer, child=node, pos='right')
        return self.float_child(currentPointer=currentPointer._parent, node=node)

    def read(self, expression: str):
        self.__expression = expression

    def print_tree(self):
        self.__prepare()
        super().print_tree()

    def build(self):
        self.reset()
        tokens = self.__tokenizer.tokenize(self.__expression)
        token_objs = self.__lexer.lex(tokens)
        self.parse(token_objs)
        self.__prev_build = self.__expression

    def evaluate(self):
        self.__prepare()
        self._root()
        return self._root._value

    def reconstruct_expression(self) -> str:
        self.__prepare()
        def __reconstruct_internal(node):
            if node._left is not None and node._right is not None:
                return '(' + __reconstruct_internal(node._left) + ' ' + str(node) + ' ' + __reconstruct_internal(node._right) + ')'
            return str(node)
        if self._root._left is None and self._root._right is None:
            return '(' + str(self._root) + ')'
        return __reconstruct_internal(node=self._root)

    def __prepare(self) -> None:
        if self.__prev_build != self.__expression:
            self.build()
        if not self.__validate_parse_tree():
            raise InvalidExpressionError('Invalid Expression')

    def __validate_parse_tree(self) -> bool:
        def __internal_recursive(node: MathNode) -> bool:
            if isinstance(node, Operator):
                if node._left is None or node._right is None:
                    return False
                return __internal_recursive(node._left) and __internal_recursive(node._right)
            elif isinstance(node, Operand):
                if node._left is None and node._right is None:
                    return True
            return False

        if self._root is None:
            return False

        return __internal_recursive(node=self._root)
