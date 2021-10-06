# Test-automatic

O programa test_tenda fazer uma pesquisa automatizada usando o filtro do site tenda.com e testa se o título do site está correto, 
após o teste é tirado um screenshot da tela.

## Test_Site

Para a usar a barra de rolagem é usado o módulo pyautogui, ele automatiza o uso de recursos do systema operacional.
Se o programa não funcionar, pode ser que a resolução da tela esteja errada, para isso use o programa Resolutio_Screen para descobrir onde está 
sua barra de rolagem no google, depois coloque o x e o y no programa test_tenda em class Test_Site > def acess_Tenda e class Test_Site > def filter

        Fuctions_Page().rolling( X, Y, roll) #Roll é o quanto quer descer a barra de rolagem
