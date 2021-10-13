# Test-automatic
Testes automatizados criados a partir do segundo desafio do meu estágio na Tenda.

### Criado em um sistema com requesitos:
 - Python 3.9.5
 - Chromedriver 94.0.4604.61
 - Principais pacotes Python: Selenium, Unittest, Pyautogui, Time

## test-API
- test_API_dolar: Teste de API de converção de dolar para real.
####
        # Faz a requesição para a API
        requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

## test-API-Zeus-nixsap
Faz o check da API e exibe a resposta do endpoint.

        {rabbitOK: true}


## test-site-tenda
O programa test_tenda.py faz uma pesquisa automatizada usando o filtro do site tenda.com e testa se o título do site está correto, 
após o teste é tirado um screenshot da tela.

        # Para executar digite no terminal
        py -m unittest (Caminho)/Test-automatic/test-site-tenda/steps/test_tenda.py


Para a usar a barra de rolagem é usado o módulo pyautogui, ele automatiza o uso de recursos do sistema operacional.
Se o programa não funcionar, pode ser que a resolução da tela esteja errada, para isso use o programa Resolution_Screen para descobrir onde está 
sua barra de rolagem no google:

        # Para executar digite no terminal
        py (Caminho)/Test-automatic/Resolution_Screen.py

Depois coloque o x e o y no programa test_tenda.py em class Test_Site > def acess_Tenda e class Test_Site > def filter

        Fuctions_Page().rolling( X, Y, roll) #Roll é o quanto quer descer a barra de rolagem
