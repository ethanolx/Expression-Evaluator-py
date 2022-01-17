# type: ignore
from typing import List, Literal
from .math_node import MathNode
from .tree import Tree
from .tokenizer import Tokenizer
from .lexer import Lexer
from .operator_ import Operator


class ParseTree(Tree):
    def __init__(self,
                 depth_symbol: str = '.',
                 mode: Literal[1, 2] = 1) -> None:
        super().__init__(depth_symbol=depth_symbol)
        self.__token_lookup = [None, {
            '+': Operator('+', lambda a, b: a._value + b._value, priority=1),
            '-': Operator('-', lambda a, b: a._value - b._value, priority=1),
            '*': Operator('*', lambda a, b: a._value * b._value, priority=2),
            '/': Operator('/', lambda a, b: a._value / b._value, priority=2),
            '**': Operator('**', lambda a, b: a._value ** b._value, priority=3)
        }, {
            '+': Operator('+', lambda a, b: max(a._value, b._value), priority=1),
            '-': Operator('-', lambda a, b: min(a._value, b._value), priority=1),
            '*': Operator('*', lambda a, b: round(a._value * b._value), priority=2),
            '/': Operator('/', lambda a, b: round(a._value / b._value), priority=2),
            '**': Operator('**', lambda a, b: a._value % b._value, priority=3)
        }][mode]
        self.__tokenizer = Tokenizer(self.__token_lookup)
        self.__lexer = Lexer(self.__token_lookup)
        self.__expression = ''

    def validate_expression(self):
        return self.__expression.replace(' ', '') == self.reconstruct_expression().replace(' ', '')

    def parse(self, token_objs: List[MathNode], i: int = 0):
        while i < len(token_objs):
            n = token_objs[i]
            if n == '(':
                i += 1
                sub_tree, i = ParseTree().parse(token_objs=token_objs, i=i)
                sub_tree.root._priority += 3
                self.insert(sub_tree.root)
            elif n == ')':
                return self, i
            else:
                self.insert(n)
            i += 1
        return self, i

    def insert(self, node: MathNode):
        if self.root is None:
            self.assign_root(node=node)
        elif self.currentPointer.left is None:
            self.currentPointer = self.assign_child(parent=node, child=self.currentPointer, pos='left')
            self.root = self.currentPointer
        elif self.currentPointer.right is None:
            self.currentPointer = self.assign_child(parent=self.currentPointer, child=node, pos='right')
        else:
            self.currentPointer = self.float_child(currentPointer=self.currentPointer, node=node)

    def assign_root(self, node: MathNode) -> 'ParseTree':
        self.root = node
        self.currentPointer = node
        return self

    def assign_child(self, parent: MathNode, child: MathNode, pos: Literal['left', 'right']) -> 'MathNode':
        child.parent = parent
        if pos == 'left':
            parent.left = child
            return parent
        elif pos == 'right':
            if parent.right is not None:
                child.left = parent.right
            parent.right = child
            return parent if child.left is None else child
        raise ValueError('Pos')

    def float_child(self, currentPointer: MathNode, node: MathNode) -> 'MathNode':
        if currentPointer is None:
            self.root = self.assign_child(parent=node, child=self.root, pos='left')
            return self.root
        if node > currentPointer:
            return self.assign_child(parent=currentPointer, child=node, pos='right')
        return self.float_child(currentPointer=currentPointer.parent, node=node)

    def read(self, expression: str):
        self.__expression = expression

    def build(self):
        tokens = self.__tokenizer.tokenize(self.__expression)
        token_objs = self.__lexer.lex(tokens)
        self.parse(token_objs)

    def evaluate(self, strict=False):
        if strict and not self.validate_expression():
            raise ValueError(f'Invalid Expression: Did you mean \'{self.reconstruct_expression()}\'')
        return self()

    def reconstruct_expression(self) -> str:
        def __reconstruct_internal(node):
            if node.left is not None and node.right is not None:
                return '(' + __reconstruct_internal(node.left) + ' ' + str(node) + ' ' + __reconstruct_internal(node.right) + ')'
            return str(node)
        if self.root.left is None and self.root.right is None:
            return '(' + str(self.root) + ')'
        return __reconstruct_internal(node=self.root)
