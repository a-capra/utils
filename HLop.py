# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:35:43 2017

@author: andrea
"""

import os
import re
import shutil

#path = 'C:/Users/andrea/Videos'
path = 'C:/Users/andrea/Downloads'
#print(os.listdir(path))
#wdir = os.listdir(path)[3]
wdir = os.listdir(path)[-1]
destination = 'D:/NewShows/Orange.is.the.New.Black.S05'

print(path + '/' + wdir)
print("----------------------------------------------------")
print(os.listdir(path + '/' + wdir))
print("----------------------------------------------------")
print("----------------------------------------------------")

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
			