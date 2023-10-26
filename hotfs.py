#!/usr/bin/env python
from __future__ import print_function
import time
from os import listdir
from sys import argv, exit

dir2list=[]
if len(argv) > 1:
    for d in range(1,len(argv)):
        #print(argv[d])
        dir2list.append(argv[d])
else:
    dir2list=['/z10tb/agdaq/data','/z10tb/agdaq/history']

with open("hotfs.log", "a") as fout:

    fout.write(time.strftime('%d-%m-%Y %H:%M:%S ',time.localtime()))
    
    for d in dir2list:
        start=time.time()
        try:
            listdir(d)
        except OSError as e:
            fout.write(" --> %s doesn't exist <-- "%d)
            continue
        stop=time.time()
        #print('data: %1.3f ms'%((stop-start)*1.e3))
        fout.write('%1.3fms '%((stop-start)*1.e3))
    fout.write("\n")



# crontab -e
# * * * * * /home/agdaq/andrea/utils/hotfs.py
