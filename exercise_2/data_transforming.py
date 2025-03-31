import pdfplumber
import pandas as pd
import os
import sys

# Adiciona o diretório pai ao path para importar funções utilitárias
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.compressToZip import compressToZip  # Função para comprimir arquivos em .zip

# Pega o diretório onde o script está localizado
script_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos de entrada e saída
path_pdf = os.path.join(script_dir, '..', 'data', 'anexos', 'anexo_I.pdf')

output_original_file_path = os.path.join(script_dir, '..', 'data', 'data_transformed.csv')
output_edited_file_path = os.path.join(script_dir, '..', 'data', 'data_transformed_edited_columns.csv')
output_zip_path = os.path.join(script_dir, '..', 'data', 'Teste_Everson_Do_Nascimento.zip')

all_rows = []        # Lista para armazenar todas as linhas extraídas
header_main = None   # Armazena o cabeçalho principal (usado como referência)

# Verifica se o PDF foi baixado previamente (Exercício 1)
if not os.path.exists(path_pdf):
    print("Arquivo do anexo I não encontrado! Verifique se você executou o script do exercício 1 primeiro.")
    exit()

# Remove arquivos de saída anteriores, se existirem
if os.path.exists(output_original_file_path):
    os.remove(output_original_file_path)

if os.path.exists(output_edited_file_path):
    os.remove(output_edited_file_path)

# Abre o PDF e inicia extração de tabelas
with pdfplumber.open(path_pdf) as pdf:
    print("Aguarde...")

    for page in pdf.pages:
        tables = page.extract_tables()

        for table in tables:
            if not table:
                continue

            # Define o cabeçalho principal a partir da primeira tabela encontrada
            if header_main is None:
                header_main = table[0]

            # Se o cabeçalho já foi definido, evita duplicá-lo nas linhas
            start = 1 if table[0] == header_main else 0

            # Adiciona apenas linhas com conteúdo não vazio
            for row in table[start:]:
                if any(cell is not None and str(cell).strip() != "" for cell in row):
                    all_rows.append(row)
    
    print("Pronto!")

# Remove a primeira linha (possivelmente repetida do cabeçalho)
data = all_rows[1:]

# Cria um DataFrame com os dados extraídos
df = pd.DataFrame(data, columns=header_main)

# Salva a versão original da tabela como CSV
df.to_csv(output_original_file_path, index=False)
print("Arquivo criado com sucesso!")

# Reabre o CSV para ajustar nomes de colunas específicas
df = pd.read_csv(output_original_file_path)

# Renomeia colunas para facilitar a leitura/interpretação
df.rename(columns={ 'OD': 'ODONTOLÓGICA', 'AMB': 'AMBULATORIAL'}, inplace=True)

# Salva uma nova versão com os nomes de colunas ajustados
df.to_csv(output_edited_file_path, index=False)

# Comprime o arquivo original em um .zip
compressToZip(output_original_file_path, output_zip_path)
