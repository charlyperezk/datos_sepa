from utils.directory import Directory as Dir
from utils.zip_files import ZipFile
from utils.regex import filter_by_keyword
from config import paths


def sepa_decompress(gross_path: str, extracted_path: str, decompressed_path: str, zip_file_name: str):
    zip_file = ZipFile(Dir.path_(gross_path, zip_file_name))
    zip_file.decompress(extracted_path)
    sepafile_extracted: list[str] = Dir.files_in_directory(extracted_path)
    list(map(lambda file: ZipFile(Dir.path_(extracted_path, file)).decompress(decompressed_path), sepafile_extracted))


if __name__ == "__main__":
    # sepa_decompress(
    #     gross_path=paths["gross"],
    #     extracted_path=paths["extracted"],
    #     decompressed_path=paths["decompressed"],
    #     zip_file_name="sepa_jueves.zip"
    #     )

    from etl import SepaETL, Configs

    file_list: list[str] = Dir.files_in_directory(paths["decompressed"])
    file_paths_list: list[str] = list(map(lambda file: Dir.path_(paths["decompressed"], file), file_list))    
    files: list[str] = filter_by_keyword("comercio", file_paths_list) # Path list


    lines = SepaETL.apply_transformations(config=Configs.ComerciosConfig, paths=files, acc=set())
    print(len(lines))
