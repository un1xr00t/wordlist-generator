# extract_wordlists.py

import tarfile
import gzip
import shutil
import os

def extract_tar_gz(file_path, extract_to):
    if file_path.endswith("tar.gz"):
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path=extract_to)
        print(f"Extracted: {file_path}")
    elif file_path.endswith(".gz"):
        with gzip.open(file_path, 'rb') as f_in:
            with open(file_path[:-3], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"Extracted: {file_path}")
    else:
        print(f"Not a tar.gz or .gz file: {file_path}")

# Extract the downloaded wordlists
for file_name in os.listdir('wordlists'):
    extract_tar_gz(os.path.join('wordlists', file_name), 'wordlists')
