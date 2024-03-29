# type: ignore
'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from typing import List, Literal
import re

from .exceptions import InvalidExpressionError, InvalidOptionError
from .math_node import MathNode
from .operator_ import Operator
from .operand_ import Operand
from .tokenizer import Tokenizer
from .lexer import Lexer
from .tree import Tree
from .expression import Expression
from .utils.mergesort import mergeSort

# For registering custom operators
import math
from math import *


class ParseTree(Tree):
    def __init__(self,
                 depth_symbol: str = '.',
                 mode: int = 1,
                 precision: int = 5) -> None:
        super().__init__(depth_symbol=depth_symbol)
        self.__precision = precision
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

    # General parse tree utilities
    # Inserts a new node
    # Time complexity: O(h), h=tree height
    def insert(self, node: MathNode):
        if self._root is None:
            self.__assign_root(node=node)
        elif self.currentPointer._left is None:
            self.currentPointer = self.__assign_child(parent=node, child=self.currentPointer, pos='left')
            self._root = self.currentPointer
        elif self.currentPointer._right is None:
            self.currentPointer = self.__assign_child(parent=self.currentPointer, child=node, pos='right')
        else:
            self.currentPointer = self.__float_child(currentPointer=self.currentPointer, node=node)

    # Assigns a new node to become the root node
    def __assign_root(self, node: MathNode) -> 'ParseTree':
        self._root = node
        self.currentPointer = node
        return self

    # Assigns child and parent nodes
    def __assign_child(self, parent: MathNode, child: MathNode, pos: Literal['left', 'right']) -> 'MathNode':
        child._parent = parent
        if pos == 'left':
            parent._left = child
            return parent
        elif pos == 'right':
            if parent._right is not None:
                child._left = parent._right
            parent._right = child
            return parent if child._left is None else child

    # Floats a node to its appropriate position
    # Time complexity: O(h), h=tree height
    def __float_child(self, currentPointer: MathNode, node: MathNode) -> 'MathNode':
        if currentPointer is None:
            self._root = self.__assign_child(parent=node, child=self._root, pos='left')
            return self._root
        if node > currentPointer:
            return self.__assign_child(parent=currentPointer, child=node, pos='right')
        return self.__float_child(currentPointer=currentPointer._parent, node=node)

    # Reads a given expression
    def read(self, expression: str):
        self.__expression = re.sub('\\s', ' ', expression)

    # Parses a list of token objects and constructs the parse tree
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

    # Combines:
    #   - Resetting
    #   - Tokenization
    #   - Lexical Analysis
    #   - Parsing/Construction
    #   - Validation
    def build(self):
        self.reset()
        tokens = self.__tokenizer.tokenize(self.__expression)
        token_objs = self.__lexer.lex(tokens)
        self.parse(token_objs)
        if not self.__validate_parse_tree():
            raise InvalidExpressionError('Invalid Expression')
        self.__prev_build = self.__expression

    # Builds the parse tree if it is not already built
    def __prepare(self) -> None:
        if self.__prev_build != self.__expression:
            self.build()

    # Validates the structure of the parse tree
    #   - Operands have no child nodes
    #   - Operators have exactly 2 child nodes
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

    # Option 1 - Assert given expression is fully parenthesised
    def validate_fully_parenthesised(self):
        return self.__expression.replace(' ', '') == self.reconstruct_expression().replace(' ', '')

    # Options 1, 2, 3 - Evaluate/Display the parse tree for given expression(s)
    # Prints the tree (uses superclass Tree to do so)
    def print_tree(self):
        self.__prepare()
        super().print_tree()

    # Evaluates the expression
    def evaluate(self):
        self.__prepare()
        self._root()
        result = self._root._value
        return result if type(result) is int else round(result, self.__precision)

    # Option 3 - Evaluate and Sort a list of expressions from a specified text file
    def evaluate_and_sort(self):
        try:
            inputfile = input("Please enter input file:\t".expandtabs(4))
            outputfile = input("Please enter output file:\t".expandtabs(4))
            filename = open(inputfile, 'r').read().splitlines()

            lst = []
            for i in filename:
                self.read(i)
                exp = Expression(i, self.evaluate())
                lst.append(exp)

            mergeSort(lst)

            print("\n>>> Evaluation and sorting started:", end='')
            header = '\n\n*** Expressions with value ==> '
            exp = []
            prev_value = None
            for i in lst:
                current_value = i.get_result()
                if current_value != prev_value:
                    var = header + str(current_value)
                    exp.append(var)
                    prev_value = current_value
                exp.append("\n" + str(i))

            processed_expressions = ''.join(exp)
            print(processed_expressions)
            print("\n>>> Evaulation and sorting completed!")
            if outputfile != '':
                with open(outputfile, "w") as add_to_output_file:
                    add_to_output_file.write(processed_expressions[2:])
        except (ValueError, InvalidExpressionError):
            print('Input file contains one or more invalid expressions. Aborting...')

    # Option 4 - Fully parenthesise a non-fully parenthesised expression
    def reconstruct_expression(self) -> str:
        self.__prepare()

        def __reconstruct_internal(node):
            if node._left is not None and node._right is not None:
                return '(' + __reconstruct_internal(node._left) + ' ' + str(node) + ' ' + __reconstruct_internal(node._right) + ')'
            return str(node)
        if self._root._left is None and self._root._right is None:
            return '(' + str(self._root) + ')'
        return __reconstruct_internal(node=self._root)

    # Option 6 - Register a New Operator
    # Allows the user to select the symbol for their custom operator
    def __get_symbol(self):
        symbol = input('Select a symbol besides [{}, ., (, )] with max length of 3: '.format(', '.join(self.__token_lookup.keys()))).strip()
        if symbol in '.()' or symbol in self.__token_lookup.keys():
            raise InvalidOptionError(f'Illegal symbol encountered: {symbol}')
        if len(symbol) > 3:
            raise InvalidOptionError(f'Symbol {symbol} is too long (max 3)')
        return symbol

    # Allows the user to select what their custom operator does
    #   - They have access to Python's standard math library's functions
    def __get_func(self):
        return eval('lambda a, b: ' + input('Enter function (in Python format) (parameters are a and b): '))

    # Allows the user to select the priority of their custom operator
    def __get_priority(self):
        self.__print_priority_menu()
        priority_str = input('Operator Priority: ').strip()
        priority = int(priority_str) if priority_str != '' else 1
        if priority not in {1, 2, 3}:
            raise SyntaxError('Invalid priority (expected 1, 2 or 3)')
        return priority

    # Prints all available priority options
    @staticmethod
    def __print_priority_menu():
        print('Enter the priority of your operator\n'
              '\t1: {+, -} [Default]\n'
              '\t2: {*, /}\n'
              '\t3: {**}')

    # Interface for complete registration of a new operator
    def register_new_operator(self):
        print('Here is a simple wizard that will guide you through registering a custom operator...')
        symbol = self.__get_symbol()
        func = self.__get_func()
        priority = self.__get_priority()
        new_operator = Operator(symbol=symbol, func=func, priority=priority)
        self.__token_lookup[symbol] = new_operator
        print(f'Successfully registered new operator {symbol}')