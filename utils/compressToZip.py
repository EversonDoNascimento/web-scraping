import zipfile
import os

def compressToZip(files = str, zip_path = str):
    """
    Comprime um ou mais arquivos em um único arquivo .zip.

    Args:
        files (str ou list): Caminho para um arquivo (string) ou uma lista de caminhos de arquivos.
        zip_path (str): Caminho de destino para o arquivo .zip a ser criado.
    """
    print("Comprimindo arquivos...")

    # Garante que 'files' seja uma lista, mesmo que apenas um caminho tenha sido passado
    if isinstance(files, str):
        files = [files]

    # Cria o arquivo .zip e adiciona os arquivos informados
    with zipfile.ZipFile(zip_path, 'w') as zip:
        for file_path in files:
            # arcname define o nome do arquivo dentro do .zip (sem o caminho completo)
            arcname = os.path.basename(file_path)
            zip.write(file_path, arcname=arcname)

    print("Arquivos comprimidos com sucesso!")
