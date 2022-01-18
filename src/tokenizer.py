from typing import Set
import re


class Tokenizer:
    def __init__(self,
                 registered_tokens: Set[str]) -> None:
        self.__registered_tokens = registered_tokens

    def tokenize(self, expression: str):
        expression_simplified = re.sub('\\s', '', expression)
        matcher = r'([-]?[\d.]+|{}|[()])'.format('|'.join((f'[{symbol}]' for symbol in self.__registered_tokens)))
        return re.findall(matcher, expression_simplified)
