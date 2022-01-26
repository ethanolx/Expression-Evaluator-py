'''
   Class: DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
# Custom Errors
class InvalidOptionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InputError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InvalidExpressionError(SyntaxError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)