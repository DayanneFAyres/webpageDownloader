from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from manipula_arquivos_e_pastas import readFile, createHTMLFile
import re
from login import LoginData


def getUnitsLink():

    links = readFile('pagina.txt')

    padrao = '(/products/.+/categories/[0-9]{1,}/posts/[0-9]+)("?.+>)(.+)(</?a>)'
    resposta = re.findall(padrao, links)

    unidades = {}

    for link in resposta:

        if link[0] not in unidades:
            unidades[link[0]] = link[2].replace(' ', '_').replace('/', '')

    return unidades

login = LoginData()

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(login['site'])
email = driver.find_element(By.ID, 'member_email')
email.send_keys(login['email'])
password = driver.find_element(By.ID, 'member_password')
password.send_keys(login['password'])
driver.find_element(By.NAME, 'commit').click()

driver.implicitly_wait(10)

units = getUnitsLink()

base_link = login['base_link']
folder_name = 'Welcome'

for link, file_name in units.items():

	driver.get(base_link+link)
	driver.implicitly_wait(2)

	unit_name = 'unidade_'
	if( unit_name in file_name.lower()):

		end_str = len(unit_name) + 2
		folder_name = file_name[0:end_str]

	elif('ftd_#' in file_name.lower()):
		folder_name = 'FTD'

	createHTMLFile(folder_name, file_name, driver.page_source)

driver.quit()