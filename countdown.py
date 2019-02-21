#!/usr/bin/env python3

import datetime
import time
from sys import argv, exit

from blink import blink

def pretty(delta):
    s=delta.seconds
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print('%4d days %2d hours %2d minutes %2d seconds'%(int(delta.days),int(hours), int(minutes), int(seconds)), end="\r")

if __name__=='__main__':

    fin = [2021, 3, 1, 0, 0, 0, 0]
    #fin = [int(t) for t in argv[1:]]
    i=0
    for t in argv[1:]:
        fin[i]=int(t)
        i+=1

    target = datetime.datetime(fin[0],fin[1],fin[2],fin[3],fin[4],fin[5],fin[6])
    delta = target - datetime.datetime.now()
    pretty(delta)

    while True:
        try:
            delta = target - datetime.datetime.now()

            if delta.total_seconds()>0:
                time.sleep(1)
            else:
                print('')
                break
            
            pretty(delta)
            
        except KeyboardInterrupt:
            print('\nBye!')
            exit(0)

    blink('This is the end!')
