#Biblioteca de elementos da page da Tenda

def estado(driver):
    estado = driver.find_element_by_id('Estados_Filtro_Superior')
    estado.click()

def estado_sp(driver):
    sp = driver.find_element_by_css_selector('#Estados_Filtro_Superior > li:nth-child(11)')
    sp.click()

def cidade(driver):
    cidade = driver.find_element_by_id('Cidades_Filtro_Superior')
    cidade.click()

def cidade_sp(driver):
    cidade_sp = driver.find_element_by_css_selector('#Cidades_Filtro_Superior > li:nth-child(3)')
    cidade_sp.click()

def bairro(driver):
    bairro = driver.find_element_by_id('Bairros_Filtro_Superior')
    bairro.click()

def bairro_barra_funda(driver):
    barra_funda = driver.find_element_by_css_selector('#Bairros_Filtro_Superior > li:nth-child(5)')
    barra_funda.click()

def obra(driver):
    obra = driver.find_element_by_id('EstagioObra_Filtro_Superior')
    obra.click()

def todos_obra(driver):
    todos_obra = driver.find_element_by_css_selector('#EstagioObra_Filtro_Superior > li:nth-child(2)')
    todos_obra.click()

def renda(driver):
    renda = driver.find_element_by_id('RendaFamiliar_Filtro_Superior')
    renda.click()

def todos_renda(driver):
    todos_renda = driver.find_element_by_css_selector('#RendaFamiliar_Filtro_Superior > li:nth-child(2)')
    todos_renda.click()

