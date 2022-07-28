import re
from manipula_arquivos_e_pastas import readFile, createHTMLFile

def detUnitsLink():

    links = readFile('pagina.txt')

    padrao = '(/products/.+/categories/[0-9]{1,}/posts/[0-9]+)("?.+>)(.+)(</a>)'
    resposta = re.findall(padrao, links)

    unidades = {}

    for link in resposta:

        if link[0] not in unidades:
            unidades[link[0]] = link[2].replace(' ', '_').replace('/', '')
            print(link[0], link[2].replace(' ', '_').replace('/', ''))

    return unidades

    