from config.project_config import project_dirs
from typing import Callable
from etl.line import Line


class Config:
    encoding = "utf-8"
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
    source_file = project_dirs.raw_data_dir / "decompressed" / "comercio.csv"
    target_file = project_dirs.processed_data_dir / "comercio.csv"
    transformation_functions = [
        lambda x: x.upper()
    ]
    filter_functions = [
        lambda x: x.count("|") == 7,
        lambda x: x.strip() != "",
    ]
    

class SucursalesConfig(Config):
    source_file = project_dirs.raw_data_dir / "decompressed" / "sucursales.csv"
    target_file = project_dirs.processed_data_dir / "sucursales.csv"
    transformation_functions = [
        lambda x: x.upper(),
    ]
    filter_functions = [
        lambda x: x.count("|") == 20,
        lambda x: x.strip() != "",
    ]


class ProductosConfig(Config):
    source_file = project_dirs.raw_data_dir / "decompressed" / "productos.csv"
    target_file = project_dirs.processed_data_dir / "productos.csv"
    transformation_functions = [
        lambda x: x.upper(),
    ]
    filter_functions = [
        lambda x: x.count("|") == 16,
        lambda x: x.strip() != "",
    ]

class ETLConfig:
    @staticmethod
    def get_configs():
        return {
        'comercio': ComerciosConfig,
        'productos': ProductosConfig,
        'sucursales': SucursalesConfig
    }