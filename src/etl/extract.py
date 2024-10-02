from abc import ABC, abstractmethod
from typing import Callable
from config.project_config import project_dirs
import logging


class Extract(ABC):
    @abstractmethod
    def extract[T](self, file_path: str, func: Callable[[str], T]) -> list[T]:
        pass


class SepaExtract(Extract):
    @staticmethod
    def extract[T](file_path: str, func: Callable[[str], T]) -> list[T]:
        try:
            project_dirs.file_path_is_valid(file_path)
        except Exception as e:
            logging.error(f"Error validating path: {e}")
            raise e

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines_as_objects: list[T] = list()
                for line in file:
                    lines_as_objects.append(func(line))
                file.close()
                return lines_as_objects
            
        except Exception as e:
            logging.error(f"Error reading file: {e}")
            raise e
