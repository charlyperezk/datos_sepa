from etl.config import Config, Line
from etl.extract import Extract, SepaExtract
from etl.transform import Transform


class ETL:
    @staticmethod
    def process(config: Config, extractor: Extract, transformer: Transform) -> set[Line]:
        lines: set[Line] = extractor.extract(config.source_file, config.instantiate_line)
        lines_filtered: set[Line] = transformer.filter(lines, config.get_filter_functions())
        lines_transformed: set[Line] = transformer.transform(lines_filtered, config.get_transformation_functions())
        return lines_transformed
    
    
class SepaETL(ETL):
    @staticmethod
    def apply_transformations(paths: list[str], config: Config, acc: set[Line] = set()) -> set[Line]:
        if len(paths) == 0:
            return acc
        class Configuration(config):
            source_file = rf"{paths[0]}"
        lines: set[Line] = ETL.process(Configuration, SepaExtract, Transform)
        return SepaETL.apply_transformations(paths[1::], config, Transform.combine([acc, lines]))