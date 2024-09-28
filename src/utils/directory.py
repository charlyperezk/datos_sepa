import os
import re


class Directory:

    @staticmethod
    def path_(base_path: str, filename: str) -> str:
        return os.path.join(base_path, filename)

    @staticmethod
    def create_directory(directory: str):
        os.makedirs(directory, exist_ok=True)

    @staticmethod
    def files_in_directory(directory: str):
        return os.listdir(directory)
    
    @staticmethod
    def files_in_directory_with_extension(directory: str, extension: str):
        return [f for f in os.listdir(directory) if f.endswith(extension)]
        
    @staticmethod
    def is_file_in_directory(directory: str, filename: str):
        return filename in os.listdir(directory)

    @staticmethod
    def resolve_filename_conflict(extract_path: str, filename: str) -> str:
        dir_path = os.path.dirname(filename)
        base_name = os.path.basename(filename)
        original_name, extension = os.path.splitext(base_name)
        counter = 1
        new_filename = base_name

        pattern = re.compile(r"(.+)\((\d+)\)$")
        match = pattern.match(original_name)
        
        if match:
            base_name = match.group(1)
            counter = int(match.group(2)) + 1
        else:
            base_name = original_name

        new_filename = f"{base_name}({counter}){extension}"
        
        full_new_filename = os.path.join(dir_path, new_filename)

        while Directory.is_file_in_directory(extract_path, full_new_filename):
            match = pattern.match(base_name)
            if match:
                counter = int(match.group(2)) + 1
            new_filename = f"{base_name}({counter}){extension}"
            full_new_filename = os.path.join(dir_path, new_filename)
            counter += 1

        return full_new_filename