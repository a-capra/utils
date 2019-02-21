
import os
import re
import shutil

path = 'C:/Users/andrea/apple/pucs'
wdir = os.listdir(path)
destination = 'C:/Users/andrea/apple/gaff'

for	ff in os.listdir(path):
	print(ff)
	searchObj = re.search('gif$',ff)
	if searchObj:
		print('moving ' + path + '/' + ff + ' to ' + destination)
		shutil.copy2(path + '/' + ff, destination)
		#os.remove(path + '/' + ff)

