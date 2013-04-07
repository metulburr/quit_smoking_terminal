import shutil
import urllib.request
import urllib.parse
import os
import sys
import zipfile
from data.version_history import VERSION

#VERSION = '0.2.4'

url = 'http://www.metulburr.com/download/quit_smoking_terminal_v{}.zip'.format(VERSION)
url_search = 'quit_smoking_terminal_v'
filename = os.path.split(url)[1]



def is_valid_url(url):
	#url = urllib.parse.urlparse(url).netloc
	if url.startswith('http://www.'):
		pass
	elif url.startswith('www'):
		url = 'http://' + url
	else:
		url = 'http://www.' + url
	try:
		status = urllib.request.urlopen(url).getcode()
		return True
	except urllib.error.URLError:
		return False
		
def get_new_url(url, url_search):
	'''upon determining need of update, located new file from html without 3rd party libs'''
	
	#get html
	path = os.path.split(url)[0]
	res = urllib.request.urlopen(path)
	html = res.read().decode()
	
	#get new file name
	html_stripped_before = html[html.find(url_search):]
	new_filename = html_stripped_before[:html_stripped_before.find('.zip') + 4]
	
	new_url = urllib.parse.urljoin(path, new_filename)
	return new_url
	
def update(new_url, new_filename_zip, old_filename):
	
	#download
	print('Downloading {}'.format(new_filename_zip))
	f = urllib.request.urlopen(new_url)
	with open(new_filename_zip,'wb') as lf:
		shutil.copyfileobj(f,lf)
	
	#extract zip
	print('Extracting {}'.format(new_filename_zip))
	top_dir = os.path.abspath('..') #go up 2 dirs, where the program file parent dir sets
	my_zip = os.path.split(new_url)[1]
	zip_file = zipfile.ZipFile(my_zip, 'r')
	for files in zip_file.namelist():
		zip_file.extract(files, top_dir)
	zip_file.close()
	
	#set paths and names
	new_dir = os.path.splitext(my_zip)[0]
	old_file = os.path.splitext(old_filename)[0]
	old_path = os.path.join(top_dir, old_file)
	new_dir_path = os.path.join(top_dir, new_dir)
	
	'''
	#restart
	import subprocess
	import threading
	path = os.path.join(new_dir_path, 'quitsmoking.py')
	os.chdir(new_dir_path)

	def restart(arg):
		subprocess.Popen(['python3', arg])
	
	threading.Thread(target=restart, 
	args=(path, ),
		).start()
	'''
	
	#delete old
	if os.path.exists(old_path):
		print('Deleting {}'.format(old_file))
		shutil.rmtree(old_path)




if not is_valid_url(url): #there is a newer version
	choice = input('Update available for program. Would you like to update now? [y/n]: ')
	if choice.lower() == 'y':
		new_url = get_new_url(url, url_search)
		new_filename = os.path.split(new_url)[1]
		update(new_url, new_filename, filename)


