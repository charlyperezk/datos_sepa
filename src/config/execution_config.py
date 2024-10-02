import sys
import logging
from config.project_config import project_dirs
from etl.config import ETLConfig
from etl.etl import SepaETL, SepaExtract, Transform


class CLI:
    @staticmethod
    def parse_arguments():
        import argparse
        parser = argparse.ArgumentParser(description="SEPA ETL Process")
        parser.add_argument('--create-dirs', action='store_true',
                            help='Create project directories (use only for first-time setup)')
        parser.add_argument('--configs', nargs='+', choices=['comercio', 'productos', 'sucursales'],
                            help='Specify which configs to process')
        parser.add_argument('--clean-raw-data', nargs='+', choices=['compressed', 'decompressed'],
                            help='Clean raw data directories')
        parser.add_argument('--process-all', action='store_true',
                            help='Process all configs')
        return parser.parse_args()
    
    @staticmethod
    def execute_process(args):
        if args.create_dirs:
            project_dirs._create_dirs()
            logging.info("Project directories created.")
            sys.exit(0)
        
        if args.configs:
            configs = [ETLConfig.get_configs()[config] for config in args.configs if config in ETLConfig.get_configs()]
            if not configs:
                logging.error("Invalid argument for --configs. Use 'comercio', 'productos' or 'sucursales'.")
                sys.exit(1)
            else:
                for config in configs:
                    lines = SepaETL.process(config, SepaExtract, Transform)
                    SepaETL.load(config, lines)

        if args.clean_raw_data:
            if 'compressed' in args.clean_raw_data:
                project_dirs.clean_raw_compressed_data()
            if 'decompressed' in args.clean_raw_data:
                project_dirs.clean_raw_decompressed_data()
            else:
                logging.error("Invalid argument for --clean-raw-data. Use 'compressed', 'decompressed' or both.")
                sys.exit(1)

        if args.process_all:
            for config in ETLConfig.get_configs().values():
                lines = SepaETL.process(config, SepaExtract, Transform)
                SepaETL.load(config, lines)