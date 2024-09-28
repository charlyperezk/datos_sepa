import re

def filter_by_keyword(keyword: str, file_list: list[str]):
    pattern = re.compile(fr"{keyword}(\\(\d+\\))?")    
    return list(filter(lambda string: pattern.search(string), file_list))
