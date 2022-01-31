'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''


# Exception class for invalid options
class InvalidOptionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


# Exception class for invalid expressions
class InvalidExpressionError(SyntaxError):
    def __init__(self, message='Invalid Expression', *args: object) -> None:
        super().__init__(message, *args)
