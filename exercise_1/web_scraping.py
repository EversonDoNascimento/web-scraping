from bs4 import BeautifulSoup
import requests
import os
import sys

# Adiciona o diretório pai ao path para permitir importar o módulo utilitário
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.compressToZip import compressToZip  # Função responsável por comprimir arquivos em .zip

# Define o diretório onde os arquivos PDF serão salvos
pdf_dir = '../data/anexos'
os.makedirs(pdf_dir, exist_ok=True)  # Cria o diretório se ele ainda não existir

# Caminho do arquivo zip final
zip_path = '../data/anexos_compressed.zip'

# Realiza a requisição HTTP para acessar a página da ANS
response = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')

# Verifica se a requisição foi bem-sucedida
if(response.status_code == 200):
    # Faz o parsing do conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Busca os links dos anexos PDF na página
    anexo1 = soup.find('a', string='Anexo I.')
    anexo2 = soup.find('a', string='Anexo II.')

    # Define os caminhos de saída dos arquivos
    out_anexo1 = os.path.join(pdf_dir, 'anexo_I.pdf')
    out_anexo2 = os.path.join(pdf_dir, 'anexo_II.pdf')
    downloaded_files = []

    # Verifica se os links foram encontrados corretamente
    if(anexo1 and anexo2 and anexo1['href'] and anexo2['href']):
        # Baixa os arquivos PDF
        pdf_anexo1 = requests.get(anexo1['href'])
        pdf_anexo2 = requests.get(anexo2['href'])

        # Verifica se o download dos arquivos foi bem-sucedido
        if(pdf_anexo1.status_code == 200 and pdf_anexo2.status_code == 200):
            # Salva o conteúdo dos PDFs no disco
            with open(out_anexo1, 'wb') as f:
                f.write(pdf_anexo1.content)
            with open(out_anexo2, 'wb') as f:
                f.write(pdf_anexo2.content)

            # Adiciona os arquivos à lista de baixados
            downloaded_files.append(out_anexo1)
            downloaded_files.append(out_anexo2)

            print("Download dos anexos concluído com sucesso!")

            # Comprime os arquivos baixados em um único .zip
            compressToZip(downloaded_files, zip_path)
        else:
            print(f'Erro ao baixar os PDFs: código {pdf_anexo1.status_code} e {pdf_anexo2.status_code}')   
    else:
        print('Links dos anexos não encontrados na página!')
else:
    print("Erro ao acessar a página!")
