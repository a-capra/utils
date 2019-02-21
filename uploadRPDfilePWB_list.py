#!/usr/bin/env python

import socket
import sys
import os

from uploadRPDfilePWBuserpage import uploadRPDfilePWBuserpage
from uploadRPDfilePWBfactorypage import uploadRPDfilePWBfactorypage
import multiprocessing as mp


def multi_run_wrapper_u(args):
   return uploadRPDfilePWBuserpage(*args)

def multi_run_wrapper_f(args):
   return uploadRPDfilePWBfactorypage(*args)

def usage():
   print "Usage:\n\tuploadRPDfilePWB_list.py list <u/f> <rpdfile> <githash>"

if __name__ == '__main__':
   if socket.gethostname() == 'alphagdaq.cern.ch':
      print 'Good! We are on', socket.gethostname()
   else:
      sys.exit('Wrong host %s'%socket.gethostname()) 

   print 'Running ', sys.argv[0]

   if len(sys.argv) != 5 :
      usage()
      sys.exit(len(sys.argv))
   
   listfile = 'pwb2update.list'
   page = "u"
   rpdfile=os.environ['HOME']+'/online/firmware/pwb_rev1/pwb_rev1_20180628_ae04285d/feam_rev1_auto.rpd'
   newgithash='ae04285dad9fed39eb3b4dd7a56c50bb3d1b53f8'
   listfile = sys.argv[1]
   page = sys.argv[2]
   rpdfile = sys.argv[3]
   newgithash = sys.argv[4]

   print "page:  ", page
   print "file:  ", rpdfile
   print "hash:  ", newgithash
   
   params=[]
   
   count=0
   with open(listfile) as f: 
      for pwb in f: 
         print pwb 
         args=[pwb.strip(), rpdfile, newgithash]
         params.append(args)
         count+=1
         
   print params, 'total: ', len(params)
   pool = mp.Pool(processes=count)
   if(page == "u"):
      pool.map(multi_run_wrapper_u, params)
      print page
   elif(page == "f"):
      print '@@@@@ ARE YOU SURE??? @@@@'
      #pool.map(multi_run_wrapper_f, params)
      print page
   else:
      usage()
