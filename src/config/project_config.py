from pathlib import Path


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
                print(f"Created directory: {directory}")
            else:
                # print(f"Directory already exists: {directory}")
                pass

    def clear_logs(self):
        """Clear the logs directory."""
        for log_file in self.logs_dir.glob('*'):
            log_file.unlink()  # Delete each file
        print(f"Cleared all logs from: {self.logs_dir}")

    def list_files_in_output(self):
        """List all files in the output directory."""
        return [file for file in self.output_dir.iterdir() if file.is_file()]

    def move_to_output(self, file_path: str):
        """Move a file to the output directory."""
        file = Path(file_path)
        if file.exists():
            file.rename(self.output_dir / file.name)
            print(f"Moved {file.name} to {self.output_dir}")
        else:
            print(f"File {file} does not exist")

    def validate_dirs(self):
        """Ensure all necessary directories exist."""
        missing_dirs = [d for d in [self.data_dir, self.logs_dir, self.config_dir, self.output_dir] if not d.exists()]
        if missing_dirs:
            print(f"Missing directories: {missing_dirs}")
        else:
            print("All directories are present.")

project_dirs = ProjectDirs(Path.cwd())