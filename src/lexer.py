'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from typing import Dict
from .operator_ import Operator
from .operand_ import Operand


# Performs lexical analysis on extracted tokens,
#   converting them into their actual objects
class Lexer:
    def __init__(self,
                 token_lookup: Dict[str, Operator]) -> None:
        self.__token_lookup = token_lookup

    # Returns a copy of the object of the associated operand or operator
    def __lex_token(self, token):
        return self.__token_lookup[token].copy()

    # Iterates through a given list of tokens, and
    #   conducts lexical analysis
    def lex(self, tokens):
        lexed_token_list = []

        for token in tokens:
            if token in '()':
                lexed_token_list.append(token)
            elif token in self.__token_lookup.keys():
                lexed_token_list.append(self.__lex_token(token=token))
            else:
                lexed_token_list.append(Operand(value=float(token) if '.' in token else int(token)))

        return lexed_token_list
