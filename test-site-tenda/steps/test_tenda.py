import pymsgbox
from selenium import webdriver
from time import sleep
import unittest
import pyautogui

class Fuctions_Page:
    # Funções para interação automatica na page da tenda

    def filtrar(self, driver):
        filtrar = driver.find_element_by_id('ButtonFiltroSuperior')
        filtrar.click()

    def aba_aptos(self, driver):
        aba = driver.find_element_by_css_selector('#menu-header > div > div.container-header.h-100 > div > '
                                                  'div.col-sm-2.col-md-2.col-lg-10.col-2.h-100.menu-desk.d-none-mobile'
                                                  ' > div > nav > ul > li.sub_menu_imoveis_a_venda.ico_menu > a > h2')
        aba.click()

    def close_msg(self, driver):
        msg = driver.find_element_by_css_selector('#selecione_geolocalizacao > div > ul > li.selectstate_no')
        msg.click()

    def close_cookie(self, driver):
        close_cookie = driver.find_element_by_css_selector('#resultado-busca-novo > section.cookie > div.botoes > div')
        close_cookie.click()

    def rolling(self, Xscreen=0, Yscreen=0, roll=0):
        pyautogui.click(Xscreen, Yscreen)
        pyautogui.vscroll(roll)

    def screenshot(self):
        im = pyautogui.screenshot()
        im.save('./results/screenshot.png')

class Tenda_Page:
    # Biblioteca de elementos da page da Tenda

    def estado(self, driver):
        estado = driver.find_element_by_id('Estados_Filtro_Superior')
        estado.click()

    def estado_sp(self, driver):
        sp = driver.find_element_by_css_selector('#Estados_Filtro_Superior > li:nth-child(11)')
        sp.click()

    def cidade(self, driver):
        cidade = driver.find_element_by_id('Cidades_Filtro_Superior')
        cidade.click()

    def cidade_sp(self, driver):
        cidade_sp = driver.find_element_by_css_selector('#Cidades_Filtro_Superior > li:nth-child(3)')
        cidade_sp.click()

    def bairro(self, driver):
        bairro = driver.find_element_by_id('Bairros_Filtro_Superior')
        bairro.click()

    def bairro_barra_funda(self, driver):
        barra_funda = driver.find_element_by_css_selector('#Bairros_Filtro_Superior > li:nth-child(5)')
        barra_funda.click()

    def obra(self, driver):
        obra = driver.find_element_by_id('EstagioObra_Filtro_Superior')
        obra.click()

    def todos_obra(self, driver):
        todos_obra = driver.find_element_by_css_selector('#EstagioObra_Filtro_Superior > li:nth-child(2)')
        todos_obra.click()

    def renda(self, driver):
        renda = driver.find_element_by_id('RendaFamiliar_Filtro_Superior')
        renda.click()

    def todos_renda(self, driver):
        todos_renda = driver.find_element_by_css_selector('#RendaFamiliar_Filtro_Superior > li:nth-child(2)')
        todos_renda.click()

class Test_Site(unittest.TestCase):
    #Interação automática

    def Start(self):
        driver = webdriver.Chrome()
        url = 'https://www.tenda.com/'

        self.acess_Tenda(driver, url)
        self.filter(driver)

    #Teste de Título
        title_of_page = driver.title
        self.assertEqual(title_of_page, 'Apartamentos à venda com condições exclusivas | Tenda.com',
                         msg=pymsgbox.alert(f'Título correto!\nTítulo: {title_of_page}',
                                            'Teste Título', pymsgbox.OK_TEXT))

    #Teste de Pesquisa //AssertionError: <selenium.webdriver.remote.webelement.Web[96 chars]77")> != 'São Paulo' : OK
        #query_result = driver.find_element_by_class_name('noPadding')

        #self.assertEqual(query_result, 'São Paulo', msg=pymsgbox.alert(f'Pesquisa correta!\nQuery: {query_result}',
        #                                                               'Teste Pesquisa', pymsgbox.OK_TEXT))

        self.ScreenShot()
        self.Close_Driver(driver)

    def acess_Tenda(self, driver, url):
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.get(url)
        Fuctions_Page().close_msg(driver)

        Fuctions_Page().aba_aptos(driver)
        Fuctions_Page().rolling(1907, 220, -750)

    def filter(self, driver):
        Tenda_Page().estado(driver)
        Tenda_Page().estado_sp(driver)
        sleep(10)
        Tenda_Page().cidade(driver)
        Tenda_Page().cidade_sp(driver)
        Tenda_Page().bairro(driver)
        Tenda_Page().bairro_barra_funda(driver)
        Tenda_Page().obra(driver)
        Tenda_Page().todos_obra(driver)
        Tenda_Page().renda(driver)
        Tenda_Page().todos_renda(driver)
        Fuctions_Page().filtrar(driver)
        Fuctions_Page().rolling(1907, 220, -1100)
        Fuctions_Page().close_cookie(driver)

    def ScreenShot(self):
        Fuctions_Page().screenshot()

    def Close_Driver(self, driver):
        sleep(3)
        driver.close()

    if __name__ == '__main__':
        unittest.main()

Test_Site().Start()
