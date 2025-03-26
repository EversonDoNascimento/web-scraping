import zipfile
import os
def compressToZip(files = str, zip_path = str):
    with zipfile.ZipFile(zip_path, 'w') as zip:
        for file_path in files:
            arcname = os.path.basename(file_path)
            zip.write(file_path, arcname=arcname)