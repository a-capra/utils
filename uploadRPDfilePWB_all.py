#!/usr/bin/env python

import socket
import sys
from getopt import getopt
import os
import pythonMidas
from uploadRPDfilePWBuserpage import uploadRPDfilePWBuserpage
from uploadRPDfilePWBfactorypage import uploadRPDfilePWBfactorypage
import multiprocessing as mp


def multi_run_wrapper_u(args):
   return uploadRPDfilePWBuserpage(*args)

def multi_run_wrapper_f(args):
   return uploadRPDfilePWBfactorypage(*args)

def usage():
   print "Usage: \tuploadRPDfilePWB_all.py [-p <u/f>] [-f <rpdfile>] [-H <githash>] [-hFn]\n"
   print "-h"
   print "--help\t\tdisplay this help\n"
   print "-p"
   print "--page\t\tpage selection u=user, f=factory\n"
   print "-f"
   print "--file\t\tRPD file path\n"
   print "-H"
   print "--githash\tRPD git hash\n"
   print "-F"
   print "--force\t\tflash all PWBs, even the ones reporting the correct hash already\n"
   print "-n"
   print "--dryrun\tcheck which boards to flash, but do not start the flashing process"

if __name__ == '__main__':
    force = False
    dryrun = False

    page = "u"
    newgithash='cabf9d3d26a24ab44ffdbfc300059276eece46fe'
    rpdfile=os.environ['HOME']+'/online/firmware/pwb_rev1/pwb_rev1_20180531_cabf9d3d_bryerton/feam_rev1_auto.rpd'

    try:
      opts, args = getopt(sys.argv[1:],"hnp:f:H:F",["help","dryrun","page=","file=","githash="])
    except getopt.GetoptError:
      usage()
      sys.exit(2)

    print opts, args

    for opt, arg in opts:
      if opt in ('-h', "--help"):
         usage()
         sys.exit()
      elif opt in ("-p", "--page"):
         page = arg
      elif opt in ("-f", "--file"):
         rpdfile = arg
      elif opt in ("-H", "--githash"):
         newgithash = arg
      elif opt in ("-F", "--force"):
         force = True
      elif opt in ("-n", "--dryrun"):
         dryrun = True

    print "page:  ", page
    print "file:  ", rpdfile
    print "hash:  ", newgithash
    print "force: ", force

    if socket.gethostname() == 'alphagdaq.cern.ch':
        print 'Good! We are on', socket.gethostname()
    else:
        sys.exit('Wrong host %s'%socket.gethostname())

    key='/Equipment/CTRL/Settings/PWB/modules'
    pwbs=pythonMidas.getString( key ).split()

    params=[]
    
    for i in pwbs:
        key='/Equipment/CTRL/Readback/%s/board/git_hash' % i
        githash=pythonMidas.getString( key )
        if (githash != newgithash or force):
            args=[i, rpdfile, newgithash]
            params.append(args)
        else:
            print i, 'with', githash, 'is good to go'

    print params, 'total: ', len(params)
    if(dryrun):
       sys.exit()
    count = 64
    pool = mp.Pool(processes=count)
    if(page == "u"):
       pool.map(multi_run_wrapper_u, params)
    elif(page == "f"):
       print '@@@@@ ARE YOU SURE??? @@@@'
       #pool.map(multi_run_wrapper_f, params)
    else:
       usage()
