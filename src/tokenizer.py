from string import ascii_lowercase
from typing import Dict, List, Literal


class Tokenizer:
    def __init__(self, token_lookup: Dict) -> None:
        self.token_lookup = token_lookup

    def tokenize(self, expression: str):
        token_list = []

        expression_simplified = expression.replace(' ', '')

        # To check if single character is recognised
        digit_set = set('0123456789.')
        letter_set = set(ascii_lowercase)
        symbol_set = set(
            ''.join(filter(lambda s: not s.isalpha(), self.token_lookup.keys())))

        # To check if tokens are recognised
        recognised_tokens = set(self.token_lookup.keys()).union(set('(,)'))

        i = 0
        j = 1

        while j <= len(expression_simplified):
            char = expression_simplified[i]
            if char not in '(,)':
                if char in digit_set:
                    while j < len(expression_simplified) and expression_simplified[j] in digit_set:
                        j += 1
                elif char in letter_set:
                    while j < len(expression_simplified) and expression_simplified[j] in letter_set:
                        j += 1
                elif char in symbol_set:
                    while j < len(expression_simplified) and expression_simplified[j] in symbol_set:
                        j += 1
                # else:
                #     raise TokenizationError(
                #         expression_simplified=expression_simplified, kind='symbol', i=i, j=j)
            token = expression_simplified[i:j]
            if token in recognised_tokens or token[0] in digit_set:
                token_list.append(token)
            else:
                for k in range(j, i, -1):
                    token = expression_simplified[i:k]
                    if token in recognised_tokens:
                        token_list.append(token)
                        j = k
                        break
                # else:
                #     raise TokenizationError(
                #         expression_simplified=expression_simplified, kind='token', i=i, j=j)
            i = j
            j += 1
        return token_list

