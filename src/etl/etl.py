import logging
from etl.config import Config, Line
from etl.extract import Extract, SepaExtract
from etl.transform import Transform
from utils.decorators import time_execution


class ETL:
    @staticmethod
    @time_execution
    def process(config: Config, extractor: Extract, transformer: Transform) -> list[Line]:
        try:
            logging.info(f"Processing {config.source_file}")
            lines: list[Line] = extractor.extract(config.source_file, config.instantiate_line)
            logging.info(f"Extracted {len(lines)} lines")
            lines_filtered: list[Line] = transformer.filter(lines, config.get_filter_functions())
            lines_transformed: list[Line] = transformer.transform(lines_filtered, config.get_transformation_functions())
            return lines_transformed
        
        except Exception as e:
            logging.error(f"Error processing {config.source_file}: {e}")
            raise e
        
    
class SepaETL(ETL):
    @staticmethod
    def apply_transformations(paths: list[str], config: Config, acc: list[Line] = list()) -> list[Line]:
        logging.debug(f"Applying transformations to {len(paths)} files")
        if len(paths) == 0:
            return acc
        class Configuration(config):
            source_file = rf"{paths[0]}"
        lines: list[Line] = ETL.process(Configuration, SepaExtract, Transform)
        logging.debug(f"Transformed {len(lines)} lines")
        return SepaETL.apply_transformations(paths[1::], config, Transform.combine([acc, lines]))
    
    @staticmethod
    def load(config: Config, lines: list[Line]):
        logging.debug(f"Loading {len(lines)} lines to {config.target_file}")
        with open(config.target_file, "w", encoding=config.encoding) as file:
            for line in lines:
                file.write(str(line))
        logging.debug(f"Loaded {len(lines)} lines to {config.target_file}")