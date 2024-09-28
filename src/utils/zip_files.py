import os
import zipfile
from utils.directory import Directory as Dir


class ZipFile:
    def __init__(self, path: str):
        self.path = path

    def decompress(self, extract_path: str, overwrite: bool = False):
        print(f"Decompressing {self.path} to {extract_path}...")
        with zipfile.ZipFile(self.path, 'r') as zip_ref:
            if overwrite:
                zip_ref.extractall(extract_path)
            else:
                temp_file = TempZipFile(self.path)
                for filename in zip_ref.namelist():
                    if Dir.is_file_in_directory(extract_path, filename):
                        new_filename = Dir.resolve_filename_conflict(extract_path, filename)
                        temp_file.write(new_filename, zip_ref.read(filename))
                        print(f"File {filename} already exists. Renamed to {new_filename}.")
                    else:
                        temp_file.write(filename, zip_ref.read(filename))
                zip_ref.close()
                temp_file.finalize()
                self.decompress(extract_path, overwrite=True)


class TempZipFile(ZipFile):
    def __init__(self, path: str):
        super().__init__(path)
        self.temp_file_path = self.path + ".temp"
        self.temp_zip_file = zipfile.ZipFile(self.temp_file_path, "w")

    def write(self, filename: str, file_content):
        self.temp_zip_file.writestr(filename, file_content)

    def finalize(self):
        self.temp_zip_file.close()
        os.remove(self.path)
        os.rename(self.temp_file_path, self.path)