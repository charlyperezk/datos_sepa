from abc import ABC, abstractmethod
from typing import Callable
from etl.config import Line


class Transform(ABC):
    @staticmethod
    def transform(lines: list[Line], funcs: set[Callable[[str], str]]) -> list[Line]:
        for func in funcs:
            lines = [line.apply(func) for line in lines]
        return lines

    @staticmethod
    def filter(lines: list[Line], funcs: set[Callable[[str], bool]]) -> list[Line]:
        for func in funcs:
            lines = [line for line in lines if line.filter(func)]
        return lines
    
    @staticmethod
    def combine(lines: list[list[Line]]) -> list[Line]:
        combined_lines = list()
        for lines_set in lines:
            combined_lines.extend(lines_set)
        return combined_lines
