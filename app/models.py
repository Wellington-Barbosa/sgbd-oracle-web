import re

def parse_tnsnames(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # capturar os nomes das bases no arquivo TNSNAMES.ora
    pattern = re.compile(r"(\w+)\s*=\s*\(DESCRIPTION", re.IGNORECASE)
    matches = pattern.findall(content)

    return matches