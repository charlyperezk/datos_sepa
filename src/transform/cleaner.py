from transform.line_parser import LineParser


class Cleaner:

    @staticmethod
    def clean(path: str, parser: LineParser, output_lines: list[str]):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parsed_line = parser.parse(line)
                if parsed_line is not None:
                    output_lines.append(parsed_line)
            f.close()
        return output_lines
    
    @staticmethod
    def capitalize(lines: list[str], output_path: str) -> list[str]:
        with open(output_path, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line)
            f.close()

