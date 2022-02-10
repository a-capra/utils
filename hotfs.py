#!/usr/bin/env python
from __future__ import print_function
import time
from os import listdir

with open("hotfs.log", "a") as fout:

    fout.write(time.strftime('%d-%m-%Y %H:%M:%S ',time.localtime()))
    
    start=time.time()
    listdir('/z10tb/agdaq/data')
    stop=time.time()
    #print('data: %1.3f ms'%((stop-start)*1.e3))
    fout.write('%1.3fms '%((stop-start)*1.e3))

    start=time.time()
    listdir('/z10tb/agdaq/history')
    stop=time.time()
    #print('history: %1.3f ms'%((stop-start)*1.e3))
    fout.write('%1.3fms\n'%((stop-start)*1.e3))



# crontab -e
# * * * * * /home/agdaq/andrea/utils/hotfs.py
