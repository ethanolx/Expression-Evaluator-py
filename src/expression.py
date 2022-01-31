'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from typing import Tuple, Union


# Wrapper class for sorting expressions based on custom function
class Expression:
    def __init__(self, expr: str, result: Union[float, int]) -> None:
        self.__expr = expr
        self.__result = result

    # Comparison function
    def comparison_tuple(self) -> Tuple[Union[float, int], int, int]:
        return self.__result, len(self.__expr), -self.__expr.count('(')

    # Comparison wrappers
    def __lt__(self, otherExpression: 'Expression') -> bool:
        return self.comparison_tuple() < otherExpression.comparison_tuple()

    def __le__(self, otherExpression: 'Expression') -> bool:
        return self.comparison_tuple() <= otherExpression.comparison_tuple()

    def __gt__(self, otherExpression: 'Expression') -> bool:
        return self.comparison_tuple() > otherExpression.comparison_tuple()

    def __ge__(self, otherExpression: 'Expression') -> bool:
        return self.comparison_tuple() >= otherExpression.comparison_tuple()

    # Getter for expression result
    def get_result(self) -> Union[float, int]:
        return self.__result

    # To be displayed as part of one of the options (evaluate and sort)
    def __str__(self) -> str:
        return self.__expr + ' ==> ' + str(self.__result)

    # Same as str
    def __repr__(self) -> str:
        return self.__str__()
