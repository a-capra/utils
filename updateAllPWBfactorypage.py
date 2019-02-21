#!/usr/bin/env python

import socket
import sys
import os
import pythonMidas
from updatePWBfactorypage import updatePWBfactorypage
import multiprocessing as mp

def multi_run_wrapper(args):
   return updatePWBfactorypage(*args)

if __name__ == '__main__':
    if socket.gethostname() == 'alphagdaq.triumf.ca':
        print 'Good! We are on', socket.gethostname()
    else:
        sys.exit('Wrong host %s'%socket.gethostname())

    key='/Equipment/CTRL/Settings/PWB/modules'
    pwbs=pythonMidas.getString( key ).split()

    # newgithash='536ace9f4b39f34a51c6b2055da6d4ab400f3c5a'
    # rpdfile=os.environ['HOME']+'/online/firmware/pwb_rev1/feam-2018-04-06-bootloader/feam_rev1_auto.rpd'
    newgithash='cabf9d3d26a24ab44ffdbfc300059276eece46fe'
    rpdfile=os.environ['HOME']+'/online/firmware/pwb_rev1/pwb_rev1_20180531_cabf9d3d_bryerton/feam_rev1_auto.rpd'
    params=[]
    
    for i in pwbs:
        key='/Equipment/CTRL/Readback/%s/board/git_hash' % i
        githash=pythonMidas.getString( key )
        if githash != newgithash:
            args=[i, rpdfile, newgithash]
            params.append(args)
        else:
            print i, 'with', githash, 'is good to go'

    print params, 'total: ', len(params)
    count = 64
    pool = mp.Pool(processes=count)
    pool.map(multi_run_wrapper, params)
