import logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=project_dirs.logs_dir / 'app.log',
    filemode='a'  
    )
import argparse
import sys
from etl import SepaETL, Configs, SepaExtract, Transform
from config.project_config import project_dirs


def parse_arguments():
    parser = argparse.ArgumentParser(description="SEPA ETL Process")
    parser.add_argument('--configs', nargs='+', choices=['comercios', 'productos', 'sucursales'],
                        help='Specify which configs to process')
    parser.add_argument('--create-dirs', action='store_true',
                        help='Create project directories (use only for first-time setup)')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    if args.create_dirs:
        project_dirs._create_dirs()
        logging.info("Project directories created.")
        sys.exit(0)

    config_map = {
        'comercios': Configs.ComerciosConfig,
        'productos': Configs.ProductosConfig,
        'sucursales': Configs.SucursalesConfig
    }

    if args.configs:
        configs = [config_map[config] for config in args.configs]
    else:
        configs = [Configs.ComerciosConfig, Configs.ProductosConfig, Configs.SucursalesConfig]

    for config in configs:
        lines = SepaETL.process(config, SepaExtract, Transform)
        SepaETL.load(config, lines)