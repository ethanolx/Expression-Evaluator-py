'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from typing import List, Set
import re


# Extracts tokens from a string expression
class Tokenizer:
    def __init__(self,
                 registered_tokens: Set[str]) -> None:
        self.__registered_tokens = registered_tokens

    # Identifies negative numbers, and
    #   groups the prefix - with the corresponding operand
    def __combine(self, tokens: List[str]) -> List[str]:
        combined = []
        prev_token = ''
        for i, token in enumerate(tokens):
            if token == '-' and (i == 0 or not prev_token[-1] in '0123456789.)'):
                tokens[i + 1] = '-' + tokens[i + 1]
            else:
                combined.append(token)
            prev_token = token
        return combined

    # Extracts plain tokens using regex
    def tokenize(self, expression: str):
        expression_simplified = re.sub('\\s', '', expression)
        known_symbols = set(''.join(self.__registered_tokens)).difference('-')
        matcher = r'([-]|[\d.]+|[{}]+|[()])'.format(''.join(known_symbols))
        plain_tokens = re.findall(matcher, expression_simplified)
        combined_tokens = self.__combine(tokens=plain_tokens)
        return combined_tokens
