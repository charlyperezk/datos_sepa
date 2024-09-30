from typing import Callable
from etl.line import Line, EmptyLine


# def create_directories():
#     list(map(lambda path: os.makedirs(path, exist_ok=True), paths.values()))

# def temporary_directories_removal():
#     Dir.delete_directory(paths["extracted"])
#     Dir.delete_directory(paths["decompressed"])

class Config:
    source_file: str
    target_file: str
    transformation_functions: set[Callable[[str], str]]
    filter_functions: set[Callable[[str], bool]]

    @staticmethod
    def instantiate_line(line: str) -> Line:
        return Line(line)

    @classmethod
    def get_source_path(cls) -> str:
        return cls.source_file
    
    @staticmethod
    def get_target_path(cls) -> str:
        return cls.target_file
    
    @classmethod
    def get_transformation_functions(cls) -> set[Callable[[str], str]]:
        return cls.transformation_functions
    
    @classmethod
    def get_filter_functions(cls) -> set[Callable[[str], bool]]:
        return cls.filter_functions


class ComerciosConfig(Config):
    source_file = "comercio.csv"
    target_file = "transformed/comercio.csv"
    transformation_functions = [
        lambda x: x.upper(),
    ]
    filter_functions = [
        lambda x: x.count("|") == 7,
        lambda x: x.strip() != "",
    ]
    

class SucursalesConfig(Config):
    source_file = "sucursales.csv"
    target_file = "transformed/sucursales.csv"
    transformation_functions = [
        lambda x: x.upper(),
    ]
    filter_functions = [
        lambda x: x.count("|") == 20,
        lambda x: x.strip() != "",
    ]


class ProductosConfig(Config):
    source_file = "productos.csv"
    target_file = "transformed/productos.csv"
    transformation_functions = [
        lambda x: x.upper(),
    ]
    filter_functions = [
        lambda x: x.count("|") == 16,
        lambda x: x.strip() != "",
    ]