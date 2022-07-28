import re
import urllib.request, re, urllib
import os
import shutil
from manipula_arquivos_e_pastas import readFile


course = 'mandarim'
root_path = '{}/{}'.format(os.getcwd(),  course)
folders = os.listdir(root_path)

# Percorre cada pasta no curso
for folder in folders:
  files = os.listdir('{}/{}'.format(root_path, folder))

  print('###### Pasta atual: {} ######'.format(folder))
  
  # Percorre cada arquivo na pasta
  for file_name in files:

    file_path = '{}/{}/{}'.format(root_path, folder, file_name)

    if(not os.path.isfile(file_path)):
      continue

    if(file_path[-5:] != '.html'):
      continue

    links = readFile(file_path).replace(' ', '')

    padrao = 'href="(https://kajabi-storefronts-production.s3.amazonaws.com/?/posts/.+/downloads/.+)"><img.+<spanclass="s2">(.+)</span></a>'
    resposta = re.findall(padrao, links)
    midias = {}
    
    for link in resposta:

      link_dwn = link[0].replace('&amp;', '&')
      link_name = link[1].replace(' ', '_').replace('/', '')

      if link_name in files:
        continue

      if link_dwn not in midias:
          
        midias[link_dwn] = link_name
        print(link_name)
        urllib.request.urlretrieve(link_dwn, link_name) 

        source = '{}/{}'.format(os.getcwd(), link_name)
        destination = '{}/{}/{}'.format(root_path, folder, link_name)
        shutil.move(source, destination)