import requests

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes_dic = cotacoes.json()
cotacao_dolar = cotacoes_dic['USDBRL']['bid']
print(f'R$ {cotacao_dolar}')
