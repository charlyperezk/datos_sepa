from config.project_config import project_dirs
import logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=project_dirs.logs_dir / 'app.log',
    filemode='a'  
    )
from etl import SepaETL, Configs, SepaExtract, Transform


if __name__ == "__main__":
    configs = [Configs.ComerciosConfig, Configs.ProductosConfig, Configs.SucursalesConfig]
    for config in configs:
        lines = SepaETL.process(config, SepaExtract, Transform)
        SepaETL.load(lines, config)