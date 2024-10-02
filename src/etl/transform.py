from abc import ABC, abstractmethod
from typing import Callable
from etl.config import Line
import logging


class Transform(ABC):
    @staticmethod
    def transform(lines: list[Line], funcs: set[Callable[[str], str]]) -> list[Line]:
        try:
            for func in funcs:
                lines = [line.apply(func) for line in lines]
            return lines

        except Exception as e:
            logging.error(f"Error transforming lines: {e}")
            raise e

    @staticmethod
    def filter(lines: list[Line], funcs: set[Callable[[str], bool]]) -> list[Line]:
        try:
            for func in funcs:
                lines = [line for line in lines if line.filter(func)]
            return lines

        except Exception as e:
            logging.error(f"Error filtering lines: {e}")
            raise e
    
    @staticmethod
    def combine(lines: list[list[Line]]) -> list[Line]:
        try:
            combined_lines = list()
            for lines_set in lines:
                combined_lines.extend(lines_set)
            return combined_lines

        except Exception as e:
            logging.error(f"Error combining lines: {e}")
            raise e
