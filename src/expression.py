from typing import Union


class Expression:
    def __init__(self, expr: str, result: Union[float, int]) -> None:
        self.__expr = expr
        self.__result = result

    def __lt__(self, otherExpression: 'Expression') -> bool:
        return self.__result < otherExpression.get_result()

    def __le__(self, otherExpression: 'Expression') -> bool:
        return self.__result <= otherExpression.get_result()

    def __gt__(self, otherExpression: 'Expression') -> bool:
        return self.__result > otherExpression.get_result()

    def __ge__(self, otherExpression: 'Expression') -> bool:
        return self.__result >= otherExpression.get_result()

    def get_result(self) -> Union[float, int]:
        return self.__result

    def __str__(self) -> str:
        return self.__expr + ' ==> ' + str(self.__result)
