
import os
import re
import shutil

#path = 'D:/aaa'
path='C:/Users/andrea/Downloads/Torrent/Marvels.Jessica.Jones.S02.Season.02.COMPLETE.XviD-AFG'
wdir = os.listdir(path)
#destination = 'D:/bbb'
destination='C:/Users/andrea/Videos/Marvels.Jessica.Jones.S02.Season.02.COMPLETE'

for id in range(len(wdir)):
	print(wdir[id])
	if os.path.isdir(path + '/' + wdir[id]):
		for	ff in os.listdir(path + '/' + wdir[id]):
			searchObj = re.search('avi$',ff)
			if searchObj:
				print(path + '/' + wdir[id] + '/' + ff)
				shutil.copy2(path + '/' + wdir[id] + '/' + ff, destination)

'''
print(path + '/' + wdir)
print("----------------------------------------------------")
print(os.listdir(path + '/' + wdir))
print("----------------------------------------------------")
print("----------------------------------------------------")
'''
'''
for fdir in os.listdir(path + '/' + wdir):
    if os.path.isfile(path + '/' + wdir + '/' + fdir):
        continue
    for ff in os.listdir(path + '/' + wdir + '/' + fdir):
        #print(ff)
        searchObj = re.search('mkv$',ff)
        if searchObj:
            print(path + '/' + wdir + '/' + fdir + '/' + ff)
            shutil.copy2(path + '/' + wdir + '/' + fdir + '/' + ff, destination)
			#shutil.copy2(path + '/' + wdir + '/' + fdir + '/' + ff, path + '/' + wdir)
'''
		