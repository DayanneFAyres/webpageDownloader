import urllib.request, re, urllib
import os
import shutil
from manipula_arquivos_e_pastas import readFile

'''
Le o html da pagina a partir de um site.
input: o link do site
output: o html da pagina
'''
def readHTMLfromUrl(site):

  with urllib.request.urlopen(site) as f:
    read_bytes = f.read()
    read_data = read_bytes.decode("utf8")

  return read_data

'''
Gera o link wistia do video presente no html
input: o arquvo html
output: link do video wistia
'''
def wistiaVideo(html_file):

  source_code = readFile(html_file).replace(' ', '')

  if source_code is None:
    return None

  wistia_pattern = 'divid="wistia_(.+)"class="wistia'
  match = re.search(wistia_pattern, source_code)

  if match is None:
    return None
  
  id_wistia = match[1]
  wistia_link = 'https://fast.wistia.net/embed/iframe/' + id_wistia
  
  return wistia_link

'''
Retorna o link do video com a qualidade especificada para download.
input: o arquivo html, 
a qualidade desejada do video (224p, 360p, 540p, 720p, 1080p)
output: link do video
'''
def linkVideo(html_file, quality):

  html = readHTMLfromUrl(wistiaVideo(html_file))

  if html is None:
    return None

  pattern_quality = 'display_name":"' + quality + '"'

  html = html[html.find(pattern_quality):]

  pattern_video = 'https://embed-ssl.wistia.com/deliveries/'
  match = re.search(pattern_video, html)
  id_index = html.find(pattern_video) + len(pattern_video)
  id_index_stop = match.string[id_index:].find('"') + id_index
  id_video = html[id_index:id_index_stop]

  link_video = pattern_video + id_video
  return link_video

course = 'italiano'
root_path = '{}/{}'.format(os.getcwd(),  course)
folders = os.listdir(root_path)

# Percorre cada pasta no curso
for folder in folders:
  files = os.listdir('{}/{}'.format(root_path, folder))
  
  # Percorre cada arquivo na pasta
  for file_name in files:

    file_path = '{}/{}/{}'.format(root_path, folder, file_name)

    if(not os.path.isfile(file_path)):
      continue

    if(file_path[-5:] != '.html' or os.path.exists(file_path[:-5]+'.mp4')):
      continue

    try:
      print(file_path)
      dwn_link = linkVideo(file_path, '540p')
    except AttributeError:
      print('\n\n!!!!!!!!!!!! Nao foi possivel baixar o video de {}. Verifique o html e baixe manualmente!!!!!!!!!!!!\n\nNext...\n'. format(file_path))
      continue
      
    urllib.request.urlretrieve(dwn_link, file_name[:-5]+'.mp4')

    source = '{}/{}.mp4'.format(os.getcwd(), file_name[:-5])
    destination = '{}/{}/{}.mp4'.format(root_path, folder, file_name[:-5])
    shutil.move(source, destination)
