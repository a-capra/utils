#!/usr/bin/env python

import socket
import sys
import pythonMidas
from initPWB_json import *

if socket.gethostname() == 'alphagdaq.triumf.ca':
    print 'Good! We are on', socket.gethostname()
else:
    sys.exit('Wrong host %s'%socket.gethostname())

key='/Equipment/CTRL/Settings/PWB/modules'
pwbs=pythonMidas.getString( key ).split()

for ipwb in pwbs:
    reboot(ipwb)
    #reboot(ipwb)
