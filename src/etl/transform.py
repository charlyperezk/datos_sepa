from abc import ABC, abstractmethod
from typing import Callable
from etl.config import Line


class Transform(ABC):
    @staticmethod
    def transform(lines: set[Line], funcs: set[Callable[[str], str]]) -> set[Line]:
        for func in funcs:
            lines = {line.apply(func) for line in lines}
        return lines

    @staticmethod
    def filter(lines: set[Line], funcs: set[Callable[[str], bool]]) -> set[Line]:
        for func in funcs:
            lines = {line for line in lines if line.filter(func)}
        return lines
    
    @staticmethod
    def combine(lines: set[set[Line]]) -> set[Line]:
        combined_lines = set()
        for lines_set in lines:
            combined_lines.update(lines_set)
        return combined_lines
