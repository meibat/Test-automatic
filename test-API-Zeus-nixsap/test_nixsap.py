import requests

headers = {
    'Accept': '*/*',
    'User-Agent': 'request',
}

url = 'http://zeusqa.tenda.com/nixsap/health/check'

resposta = requests.get(url, headers=headers)

print(resposta.text)