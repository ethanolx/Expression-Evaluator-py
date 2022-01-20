from typing import List, Literal
from .math_node import MathNode
from .operator_ import Operator
from .tokenizer import Tokenizer
from .lexer import Lexer
from .tree import Tree


class ParseTree(Tree):
    def __init__(self,
                 depth_symbol: str = '.',
                 mode: Literal[1, 2] = 1) -> None:
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
        self.__strict_mode = False
        self.__expression = ''
        self.__prev_build = ''

    def register_new_operator(self):
        print('Here is a simple wizard that will guide you through registering a custom operator...')
        symbol = input('Select a symbol besides [{}, ., (, )]:'.format(', '.join(self.__token_lookup.keys())))
        func = input('Enter function (in Python lambda format): ')
        print('Enter the priority of your operator')
        print('\t1: {+, -}'.expandtabs(4))
        print('\t2: {*, /}'.expandtabs(4))
        print('\t3: {**}'.expandtabs(4))
        priority = int(input('Operator Priority: '))
        if priority not in {1, 2, 3}:
            raise SyntaxError('Invalid priority (expected 1, 2 or 3)')
        self.__token_lookup[symbol] = Operator(symbol=symbol, func=eval(func), priority=priority)

    def validate_expression(self):
        return self.__expression.replace(' ', '') == self.reconstruct_expression().replace(' ', '')

    def parse(self, token_objs: List[MathNode], i: int = 0):
        while i < len(token_objs):
            n = token_objs[i]
            if n == '(':
                i += 1
                sub_tree, i = ParseTree().parse(token_objs=token_objs, i=i)
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
        self.reset()

    def print_tree(self):
        if self.__prev_build != self.__expression:
            self.build()
        super().print_tree()

    def build(self):
        tokens = self.__tokenizer.tokenize(self.__expression)
        token_objs = self.__lexer.lex(tokens)
        self.parse(token_objs)
        self.__prev_build = self.__expression

    def evaluate(self):
        if self.__prev_build != self.__expression:
            self.build()
        if self.__strict_mode and not self.validate_expression():
            raise ValueError(f'Invalid Expression: Did you mean \'{self.reconstruct_expression()}\'')
        self._root()
        return self._root._value

    def reconstruct_expression(self) -> str:
        def __reconstruct_internal(node):
            if node._left is not None and node._right is not None:
                return '(' + __reconstruct_internal(node._left) + ' ' + str(node) + ' ' + __reconstruct_internal(node._right) + ')'
            return str(node)
        if self._root._left is None and self._root._right is None:
            return '(' + str(self._root) + ')'
        return __reconstruct_internal(node=self._root)
