# download_wordlists.py

import requests
import os

def download_wordlist(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download: {url}")

# Example wordlist URLs from GitHub and other sources
wordlist_urls = [
    "https://github.com/danielmiessler/SecLists/raw/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz",
    "https://github.com/danielmiessler/SecLists/raw/master/Passwords/Common-Credentials/10_million_password_list_top_100000.txt",
    "https://github.com/danielmiessler/SecLists/raw/master/Passwords/Probable-Passwords/Top12Thousand-probable-v2.txt",
    "https://github.com/danielmiessler/SecLists/raw/master/Passwords/xato-net-10-million-passwords-100000.txt",
    "https://weakpass.com/wordlist/90",
    "https://weakpass.com/wordlist/91",
    "https://weakpass.com/wordlist/81",
    "https://crackstation.net/files/crackstation-human-only.txt.gz"
]

os.makedirs('wordlists', exist_ok=True)
for url in wordlist_urls:
    file_name = url.split('/')[-1]
    download_wordlist(url, os.path.join('wordlists', file_name))
