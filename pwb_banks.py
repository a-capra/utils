#!/usr/bin/env python

import socket
import sys
import pythonMidas

if socket.gethostname() == 'alphagdaq.cern.ch':
    print 'Good! We are on', socket.gethostname()
else:
    sys.exit('Wrong host %s'%socket.gethostname())

key='/Equipment/CTRL/Settings/PWB/modules'
pwbs=pythonMidas.getString( key ).split()

key='/Runinfo/Run number'
run=int(pythonMidas.getString( key ).strip())

fname='feam_banks_%06d.txt' % run
print fname
f=open(fname,'w')
f.write('# feam banks, run %d\n'%run)
icol=0
for ipwb in pwbs:
    if pwbs.index( ipwb ) % 8 == 0:
        f.write('# col %d\n'%icol)
        icol+=1
    f.write(ipwb+'\n')
f.close()
