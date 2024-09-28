from utils.directory import Directory as Dir
from utils.zip_files import ZipFile
from utils.regex import filter_by_keyword
from transform.combiner import CsvTransformer
from config import transform_config, create_directories, paths


def sepa_decompress(gross_path: str, extracted_path: str, decompressed_path: str):

    zip_file = ZipFile(Dir.path_(gross_path, "sepa_jueves.zip"))
    zip_file.decompress(extracted_path)
    sepafile_extracted: list[str] = Dir.files_in_directory(extracted_path)
    list(map(lambda file: ZipFile(Dir.path_(extracted_path, file)).decompress(decompressed_path), sepafile_extracted))


def apply_transformations(config: dict, base_path: str):
    file_list: list[str] = Dir.files_in_directory(paths["decompressed"])
    file_paths_list: list[str] = list(map(lambda file: Dir.path_(paths["decompressed"], file), file_list))

    for key, value in config.items():
        print("Applying transformation: ", value["filename"])
        files: list[str] = filter_by_keyword(key, file_paths_list)
        CsvTransformer.transform(files, value["parser"], Dir.path_(base_path, value["filename"]))

def clean_directories():
    Dir.delete_directory(paths["extracted"])
    Dir.delete_directory(paths["decompressed"])

if __name__ == "__main__":
    create_directories()
    sepa_decompress(
        gross_path=paths["gross"],
        extracted_path=paths["extracted"],
        decompressed_path=paths["decompressed"]
        )
    apply_transformations(transform_config, paths["combined"])
    clean_directories()