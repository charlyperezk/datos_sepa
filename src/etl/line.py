from abc import ABC, abstractmethod
from typing import Callable


class EmptyLine:
    def is_empty(self) -> bool:
        return True


class Line(ABC):
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"Line('{self.value}')"

    def is_empty(self) -> bool:
        return False

    def apply(self, function: Callable[[str], str]) -> "Line":
        return Line(function(self.value))
    
    def filter(self, function: Callable[[str], bool]) -> bool:
        return function(self.value)