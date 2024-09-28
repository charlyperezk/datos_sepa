# from pyspark.sql import SparkSession
from abc import ABC, abstractmethod
import pandas as pd


class FileReader(ABC):
    def __init__(self, file_path: str, encoding: str = "utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    @abstractmethod
    def load(self):
        pass


class CSVReader(FileReader):
    def __init__(self, file_path: str, encoding: str = "utf-8", sep: str = "|"):
        super().__init__(file_path, encoding)  
        self.sep = sep

    def load(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path, encoding=self.encoding, sep=self.sep)


class TxtReader(FileReader):
    def __init__(self, file_path: str, encoding: str = "utf-8"):
        super().__init__(file_path, encoding)

    def load(self): 
        with open(self.file_path, 'r', encoding=self.encoding) as file:
            for line in file:
                yield line
    
    def read(self):
        with open(self.file_path, 'r', encoding=self.encoding) as file:
            for line in file:
                print(line)


# class SparkReader(FileReader):
#     def __init__(self, file_path: str, encoding: str = "utf-8"):
#         super().__init__(file_path, encoding)

#     def load(self): ...