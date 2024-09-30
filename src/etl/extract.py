from abc import ABC, abstractmethod
from typing import Callable, TypeVar
from etl.config import Line


class Extract(ABC):
    @abstractmethod
    def extract[T](self, file_path: str, func: Callable[[str], T]) -> set[T]:
        pass


class SepaExtract(Extract):
    @staticmethod
    def extract[T](file_path: str, func: Callable[[str], T]) -> set[T]:
        with open(file_path, "r", encoding="utf-8") as file:
            lines_as_objects: set[T] = set()
            for line in file:
                lines_as_objects.add(func(line))
            file.close()
            return lines_as_objects
