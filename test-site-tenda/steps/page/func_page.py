import pyautogui

#Funções para interação automatica na page da tenda

def filtrar(driver):
    filtrar = driver.find_element_by_id('ButtonFiltroSuperior')
    filtrar.click()

def aba_aptos(driver):
    aba = driver.find_element_by_css_selector('#menu-header > div > div.container-header.h-100 > div > div.col-sm-2.col-md-2.col-lg-10.col-2.h-100.menu-desk.d-none-mobile > div > nav > ul > li.sub_menu_imoveis_a_venda.ico_menu > a > h2')
    aba.click()

def close_msg(driver):
    msg = driver.find_element_by_css_selector('#selecione_geolocalizacao > div > ul > li.selectstate_no')
    msg.click()

def close_cookie(driver):
    close_cookie = driver.find_element_by_css_selector('#resultado-busca-novo > section.cookie > div.botoes > div')
    close_cookie.click()

def rolling(Xscreen=0, Yscreen=0, roll=0):
    pyautogui.click(Xscreen, Yscreen)
    pyautogui.vscroll(roll)