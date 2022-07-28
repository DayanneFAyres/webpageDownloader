import os
import codecs

def readFile(file_name):

	try:
		with open(file_name) as f:
			read_data = f.read()
	
	except FileNotFoundError:
		return None

	return read_data

def createDirectory(folder_name):

	try:
		os.mkdir('./' + folder_name)

	except OSError:
		raise OSError('Impossivel criar diretorio {}'.format(file_name))


def createHTMLFile(folder_name, file_name, page_source):

	BASE_DIR = os.getcwd()
	dir_name = BASE_DIR + '/' + folder_name

	if(not os.path.isdir(dir_name)):
		createDirectory(folder_name)

	try:
		#get file path to save page
		n = os.path.join(dir_name, file_name + '.html')
	except OSError:
		raise OSError('Impossivel criar arquivo {}/{}.html'.format(dir_name, file_name))

	#open file in write mode with encoding
	f = codecs.open(n, "w", "utf−8")
	#write page source content to file
	f.write(page_source)

