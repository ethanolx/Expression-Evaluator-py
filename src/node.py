from abc import ABC, abstractmethod
from typing import Any


class Node(ABC):
    def __init__(self,
                 value) -> None:
        self._value = value
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return self.__str__()

    def __call__(self) -> Any:
        return self._value

    @abstractmethod
    def __lt__(self, otherNode) -> bool:
        pass

    @abstractmethod
    def __gt__(self, otherNode) -> bool:
        pass