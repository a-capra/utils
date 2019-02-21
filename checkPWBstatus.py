#!/usr/bin/env python

import socket
import sys
import subprocess as sp
import pythonMidas

if socket.gethostname() == 'alphagdaq.cern.ch':
    print 'Good! We are on', socket.gethostname()
else:
    sys.exit('Wrong host %s'%socket.gethostname())

key='/Equipment/CTRL/Settings/PWB/modules'
pwbs=pythonMidas.getString( key ).split()

key='/Equipment/CTRL/Variables/pwb_state'
stat=pythonMidas.getString( key ).split()

s=dict(zip(pwbs, stat))

tool_r='esper-tool read '

#print s
for ipwb in sorted(s.keys()):

    tool_r_build=tool_r+ipwb+' board elf_build_str'
    tool_r_githash=tool_r+ipwb+' board git_hash'

    build='0'
    try:
        build=sp.check_output(tool_r_build,stderr=sp.STDOUT,shell=True).strip().strip('"')
    except sp.CalledProcessError as e:
        #print 'Error raised in ', tool_r_build, e.output,
        print ipwb, 'stat=%s'%s[ipwb], '\t', e.output,
        continue

    '''
    if build=='0':
        print ipwb, 'stat=%s'%s[ipwb]
        continue
    '''

    githash='0'
    try:
        githash=sp.check_output(tool_r_githash,stderr=sp.STDOUT,shell=True).strip().strip('"')
    except sp.CalledProcessError as e:
        print 'Error raised in ', tool_r_githash, e.output
        githash='0'
    

    #print i, s[i], built, githash
    if githash=='0':
        print ipwb, 'stat=%s'%s[ipwb], '\t', build
    else:
        print ipwb, 'stat=%s'%s[ipwb], '\t', build, githash
