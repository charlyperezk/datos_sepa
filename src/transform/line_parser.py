from abc import ABC, abstractmethod
from typing import Optional


filter_by_pipes = lambda line: filter(lambda x: x == "|", line)
split_by_pipe = lambda line: line.split("|")
count_pipes = lambda line: len(list(filter_by_pipes(line)))


class Line(ABC):
    line: str

    def is_empty(self) -> bool:
        return self.line.strip() == ""
    
    @abstractmethod
    def has_no_pipes(self) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def is_valid(self) -> bool:
        raise NotImplementedError


class ComerciosLine(Line):
    def __init__(self, line: str):
        self.line = line

    def has_no_pipes(self) -> bool:
        return count_pipes(self.line) == 0 and self.line.strip() != ""
    
    def is_valid(self) -> bool:
        return count_pipes(self.line) == 7 and not self.is_empty()

    def __str__(self):
        return self.line


class ProductosLine(ComerciosLine):
    def __init__(self, line: str):
        self.line = line

    def is_valid(self) -> bool:
        return count_pipes(self.line) == 16 and not self.is_empty()


class SucursalesLine(ComerciosLine):
    def __init__(self, line: str):
        self.line = line

    def is_valid(self) -> bool:
        return count_pipes(self.line) == 20 and not self.is_empty()


class LineParser(ABC):
    @abstractmethod
    def parse(line: str) -> Optional[str]:
        raise NotImplementedError


class ComerciosParser(LineParser):
    @staticmethod
    def parse(line: str) -> Optional[str]:
        line: ComerciosLine = ComerciosLine(line)
        if line.is_valid():
            return line.line
        else:
            return None


class ProductosParser(LineParser):
    @staticmethod
    def parse(line: str) -> Optional[str]:
        line: ProductosLine = ProductosLine(line)
        if line.is_valid():
            return line.line
        else:
            return None
        

class SucursalesParser(LineParser):
    @staticmethod
    def parse(line: str) -> Optional[str]:
        line: SucursalesLine = SucursalesLine(line)
        if line.is_valid():
            return line.line
        else:
            return None