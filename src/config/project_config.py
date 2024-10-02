from pathlib import Path
import logging
import os


class ProjectDirs:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)

        self.resources_dir = self.base_dir / 'resources'
        self.raw_data_dir = self.resources_dir / 'raw'
        self.compressed_data_dir = self.raw_data_dir / 'compressed'
        self.decompressed_data_dir = self.raw_data_dir / 'decompressed'
        self.processed_data_dir = self.resources_dir / 'processed'
        self.bash_scripts_dir = self.base_dir / 'src' / 'etl' / 'bash_scripts'
        self.logs_dir = self.base_dir / 'logs'
        self.config_dir = self.base_dir / 'src' / 'config'
        # self.output_dir = self.base_dir / 'output'
        
        self._create_dirs()

    def _create_dirs(self):
        """Create all necessary directories if they don't exist."""
        for directory in [self.resources_dir, self.raw_data_dir, self.compressed_data_dir, self.decompressed_data_dir, self.processed_data_dir, self.logs_dir, self.config_dir]:
            if not directory.exists():
                directory.mkdir(parents=True)
                logging.info(f"Created directory: {directory}")
            else:
                logging.info(f"Directory already exists: {directory}")

    def clear_logs(self):
        """Clear the logs directory."""
        for log_file in self.logs_dir.glob('*'):
            log_file.unlink()  # Delete each file
        logging.info(f"Cleared all logs from: {self.logs_dir}")

    def list_files_in_output(self):
        """List all files in the output directory."""
        return [file for file in self.output_dir.iterdir() if file.is_file()]

    def move_to_output(self, file_path: str):
        """Move a file to the output directory."""
        file = Path(file_path)
        if file.exists():
            file.rename(self.output_dir / file.name)
            logging.info(f"Moved {file.name} to {self.output_dir}")
        else:
            logging.info(f"File {file} does not exist")

    def validate_dirs(self):
        """Ensure all necessary directories exist."""
        missing_dirs = [d for d in [self.data_dir, self.logs_dir, self.config_dir, self.output_dir] if not d.exists()]
        if missing_dirs:
            logging.info(f"Missing directories: {missing_dirs}")
        else:
            logging.info("All directories are present.")

    def file_path_is_valid(self, file_path: str) -> bool:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        if not os.path.isfile(file_path):
            raise IsADirectoryError(f"File is a directory: {file_path}")
        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"File is not readable: {file_path}")
    
    def clean_raw_compressed_data(self):
        for file in self.compressed_data_dir.iterdir():
            if file.is_file():
                file.unlink()
                logging.info(f"Deleted file: {file}")
            else:
                logging.info(f"Skipping directory: {file}")

    def clean_raw_decompressed_data(self):
        for file in self.decompressed_data_dir.iterdir():
            if file.is_file():
                file.unlink()
                logging.info(f"Deleted file: {file}")
            else:
                logging.info(f"Skipping directory: {file}")

project_dirs = ProjectDirs(Path.cwd())


class ProjectConfigs:
    @staticmethod
    def setup_logging(console_level=logging.DEBUG, file_level=logging.DEBUG):
        logging.getLogger().handlers.clear()
        
        file_handler = logging.FileHandler(project_dirs.logs_dir / 'app.log')
        file_handler.setLevel(file_level)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(console_level)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        logger = logging.getLogger()
        logger.setLevel(file_level)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
