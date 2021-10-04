import pymsgbox
from behave import *
from selenium import webdriver
from page import func_page, tenda_page
from time import sleep
import unittest

driver = webdriver.Chrome()
url = 'https://www.tenda.com/'

@given(u'acesso a página inicial da Tenda')
def step_impl(context):
    driver.implicitly_wait(30)
    driver.maximize_window()

    driver.get(url)
    func_page.close_msg(driver)


@given(u'clico na aba de apartamentos')
def step_impl(context):
    func_page.aba_aptos(driver)
    func_page.rolling(1907, 220, -750)


@given(u'coloco as preferências de filtro')
def step_impl(context):
    tenda_page.estado(driver)
    tenda_page.estado_sp(driver)
    sleep(10)
    tenda_page.cidade(driver)
    tenda_page.cidade_sp(driver)
    tenda_page.bairro(driver)
    tenda_page.bairro_barra_funda(driver)
    tenda_page.obra(driver)
    tenda_page.todos_obra(driver)
    tenda_page.renda(driver)
    tenda_page.todos_renda(driver)


@when(u'clico no botão de filtrar')
def step_impl(context):
    func_page.filtrar(driver)
    func_page.rolling(1907, 220, -1100)

@then(u'devo visualizar os resultados')
def step_impl(context):
    Test_Site().test_title()
    func_page.screenshot()
    sleep(3)
    driver.close()


class Test_Site(unittest.TestCase):

    def test_title(self):
        title_of_page = driver.title

        self.assertEqual(title_of_page, 'Apartamentos à venda com condições exclusivas | Tenda.com',
                         msg=pymsgbox.alert(f'Título correto!\n Título: {title_of_page}',
                                            'Teste Título', pymsgbox.OK_TEXT))

    if __name__ == '__main__':
        unittest.main()
