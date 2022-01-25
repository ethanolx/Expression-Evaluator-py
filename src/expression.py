from typing import Tuple, Union

class Expression:
    def __init__(self, expr: str, result: Union[float, int]) -> None:
        self.__expr = expr
        self.__result = result

    def comparison_tuple(self) -> Tuple[Union[float, int], int, int]:
        return self.__result, len(self.__expr), -self.__expr.count('(')

    def __lt__(self, otherExpression: 'Expression') -> bool:
        return self.comparison_tuple() < otherExpression.comparison_tuple()

    def __le__(self, otherExpression: 'Expression') -> bool:
        return self.comparison_tuple() <= otherExpression.comparison_tuple()

    def __gt__(self, otherExpression: 'Expression') -> bool:
        return self.comparison_tuple() > otherExpression.comparison_tuple()

    def __ge__(self, otherExpression: 'Expression') -> bool:
        return self.comparison_tuple() >= otherExpression.comparison_tuple()

    def get_result(self) -> Union[float, int]:
        return self.__result

    def __str__(self) -> str:
        return self.__expr + ' ==> ' + str(self.__result)

    def __repr__(self) -> str:
        return self.__str__()