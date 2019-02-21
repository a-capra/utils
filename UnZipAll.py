import os
import re
import zipfile

path = os.getcwd()
wdir = os.listdir(path)

for ff in wdir:
	searchObj = re.search('zip$',ff)
	if searchObj:
		print(path + '\\' + ff)
		with zipfile.ZipFile(ff,"r") as zip_ref:
			zip_ref.extractall(path)
		