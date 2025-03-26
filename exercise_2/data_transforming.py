import pdfplumber
import pandas as pd
import os

path_pdf = "../data/anexos/anexo_I.pdf"
output_original_file_path = "../data/data_transformed.csv"
output_edited_file_path = "../data/data_transformed2.csv"
all_rows = []
header_main = None

if(not os.path.exists(path_pdf)):
    print("Arquivo do anexo I não encontrado! Verifique se você executou o script do exercício 1 primeiro.")
    exit()

if(os.path.exists(output_original_file_path)):
    os.remove(output_original_file_path)

if(os.path.exists(output_edited_file_path)):
    os.remove(output_edited_file_path)

with pdfplumber.open(path_pdf) as pdf:
    print("Aguarde...")
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if(not table):
                continue
            if(header_main is None):
                header_main = table[0]               
            start = 1 if table[0] == header_main else 0
            for row in table[start:]:
                if any(cell is not None and str(cell).strip() != "" for cell in row):
                    all_rows.append(row)
    print("Pronto!")
data = all_rows[1:]
df = pd.DataFrame(data, columns=header_main)
df.to_csv(output_original_file_path, index=False)
print("Arquivo criado com sucesso!")


df = pd.read_csv(output_original_file_path)
df.rename(columns={ 'OD': 'ODONTOLÓGICA', 'AMB': 'AMBULATORIAL'}, inplace=True)
df.to_csv(output_edited_file_path, index=False)