from bs4 import BeautifulSoup
import requests
import os
import zipfile
# import shutil

pdf_dir = '../data/anexos'
os.makedirs(pdf_dir, exist_ok=True)
zip_path = '../data/anexos_compactados.zip'
response = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')

if(response.status_code == 200):
    soup = BeautifulSoup(response.text, 'lxml')
    anexo1 = soup.find('a', string='Anexo I.')
    anexo2 = soup.find('a', string='Anexo II.')
    out_anexo1 = os.path.join(pdf_dir, 'anexo_I.pdf')
    out_anexo2 = os.path.join(pdf_dir, 'anexo_II.pdf')
    downloaded_files = []
    if(anexo1  and anexo2 and anexo1['href'] and anexo2['href']):
        pdf_anexo1 = requests.get(anexo1['href'])
        pdf_anexo2 = requests.get(anexo2['href'])
        if(pdf_anexo1.status_code == 200 and pdf_anexo2.status_code == 200):
            with open(out_anexo1, 'wb') as f:
                f.write(pdf_anexo1.content)
            with open(out_anexo2, 'wb') as f:
                f.write(pdf_anexo2.content)
            downloaded_files.append(out_anexo1)
            downloaded_files.append(out_anexo2)
            print("Download dos anexos concluído com sucesso!")
            with zipfile.ZipFile(zip_path, 'w') as zip:
                for file_path in downloaded_files:
                    arcname = os.path.basename(file_path)
                    zip.write(file_path, arcname=arcname)
            # shutil.rmtree(pdf_dir)
        else:
            print(f'Error ao baixar os PDFs: código {pdf_anexo1.status_code} e {pdf_anexo2.status_code}')
        
    else:
        print('Links não encontrados!')
else:
    print("Erro ao acessar página!")