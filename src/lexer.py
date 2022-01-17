from typing import Dict, List, cast

from .operand_ import Operand
from .operator_ import Operator


class Lexer:
    def __init__(self,
                 token_lookup: Dict) -> None:
        self.token_lookup = token_lookup

    def lex_token(self, token):
        if token in self.token_lookup:
            return self.token_lookup[token].copy()
        return None
        # raise LexingError(f'Unknown token {token} encountered')

    def lex(self, tokens):
        lexed_token_list = []

        digit_set = set('0123456789.')
        i = 0

        operand_expected = True
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                operand_expected = True
                lexed_token_list.append(token)
            elif token == ')':
                operand_expected = False
                lexed_token_list.append(token)
            elif token == '-':
                if operand_expected:
                    i += 1
                    operand_expected = False
                    lexed_token_list.append(Operand(value=-(float(tokens[i]) if '.' in tokens[i] else int(tokens[i]))))
                else:
                    operand_expected = True
                    lexed_token_list.append(self.lex_token(token=token))
            elif token[0] in digit_set:
                # Normal numeric operand
                operand_expected = False
                num = float(token) if '.' in token else int(token)
                lexed_token_list.append(Operand(value=num))
            else:
                operand_expected = True
                lexed_token_list.append(self.lex_token(token=token))
            i += 1
        return lexed_token_list