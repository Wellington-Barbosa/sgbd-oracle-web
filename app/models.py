import re


def parse_tnsnames(tnsnames_path):
    with open(tnsnames_path, 'r') as file:
        content = file.read()

    # Regex para capturar as entradas do tnsnames.ora
    pattern = re.compile(r'(?P<alias>\w+)\s*=\s*\((?P<desc>.*?)\)\n\n', re.DOTALL)
    matches = pattern.finditer(content)

    tns_entries = {}

    for match in matches:
        alias = match.group('alias')
        desc = match.group('desc')

        # Capturar HOST e PORT para cada SERVICE_NAME
        host_match = re.search(r'HOST\s*=\s*(\S+)', desc)
        port_match = re.search(r'PORT\s*=\s*(\d+)', desc)
        service_name_match = re.search(r'SERVICE_NAME\s*=\s*(\S+)', desc)

        if host_match and port_match and service_name_match:
            host = host_match.group(1)
            port = int(port_match.group(1))
            service_name = service_name_match.group(1)

            tns_entries[service_name] = {
                'host': host,
                'port': port
            }

    return tns_entries
