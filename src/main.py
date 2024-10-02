from config.execution_config import CLI
from config.project_config import ProjectConfigs
ProjectConfigs.setup_logging()
import logging


if __name__ == "__main__":
    
    logging.info("Welcome to SEPA ETL")

    args = CLI.parse_arguments()
    CLI.execute_process(args)
    
    logging.info("SEPA ETL Process completed")

