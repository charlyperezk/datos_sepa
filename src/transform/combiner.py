from functools import reduce
from transform.cleaner import Cleaner
from transform.line_parser import LineParser


class CsvTransformer:
    @staticmethod
    def clean_lines(csv_paths: list[str], parser: LineParser) -> list[list[str]]:
        cleaned_lines = list(map(lambda file: Cleaner.clean(file, parser, []), csv_paths))
        return cleaned_lines

    @staticmethod
    def get_headers(cleaned_lines: list[list[str]]) -> str:
        return cleaned_lines[0][0] if len(cleaned_lines) > 0 else ""

    @staticmethod
    def combine_lines(cleaned_lines: list[list[str]]) -> list[str]:
        combined_lines = reduce(lambda x, y: x[1::] + y[1::], cleaned_lines)
        return combined_lines

    @staticmethod
    def append_headers(headers: str, combined_lines: list[str]) -> list[str]:
        return [headers] + combined_lines

    @staticmethod
    def capitalize(lines: list[str], output_path: str) -> list[str]:
        Cleaner.capitalize(lines, output_path)

    @staticmethod
    def transform(csv_paths: list[str], parser: LineParser, output_path: str):
        if len(csv_paths) == 0:
            return None
        else:
            cleaned_lines = CsvTransformer.clean_lines(csv_paths, parser)
            headers = CsvTransformer.get_headers(cleaned_lines)
            combined_lines = CsvTransformer.combine_lines(cleaned_lines)
            appended_lines = CsvTransformer.append_headers(headers, combined_lines)
            CsvTransformer.capitalize(appended_lines, output_path)