import re

def extrair_dados_tnsnames(arquivo):
    with open(arquivo, 'r') as file:
        conteudo = file.read()

    padrao = re.compile(
        r'(\w+)\s*=\s*\(\s*DESCRIPTION\s*=\s*\(.*?'
        r'HOST\s*=\s*([^\s\)]+).*?'
        r'PORT\s*=\s*([^\s\)]+).*?'
        r'SERVICE_NAME\s*=\s*([^\s\)]+).*?\)',
        re.DOTALL
    )

    correspondencias = padrao.findall(conteudo)

    dados_extraidos = []
    for nome, host, port, service_name in correspondencias:
        dados_extraidos.append({
            'NOME': nome,
            'HOST': host,
            'PORT': port,
            'SERVICE_NAME': service_name
        })

    return dados_extraidos

# Exemplo de uso
# arquivo_tnsnames = 'C:/Users/wellington.barbosa/Documents/GitHub/sgbd-oracle-web/app/files/TNSNAMES.ora'
# dados = extrair_dados_tnsnames(arquivo_tnsnames)
# for dado in dados:
#    print(f"NOME: {dado['NOME']}, HOST: {dado['HOST']}, PORT: {dado['PORT']}, SERVICE_NAME: {dado['SERVICE_NAME']}")
