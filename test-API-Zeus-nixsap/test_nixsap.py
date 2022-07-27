import requests

headers = {
    'Accept': '*/*',
    'User-Agent': 'request',
}

url = ''

resposta = requests.get(url, headers=headers)

print(resposta.text)
