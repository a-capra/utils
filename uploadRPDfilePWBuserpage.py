#!/usr/bin/env python

import socket
import sys
import os
import requests
import subprocess as sp
from pwbping import pwbping
import time

def PWBreboot(address):
    cmd='reboot_pwb'

    headers={'Content-Type':'application/json','Accept':'application/json'}
    par={'client_name':'fectrl','cmd':cmd,'args':address}
    payload={'method':'jrpc','params':par,'jsonrpc':'2.0','id': 0}

    url='http://localhost:8080?mjsonrpc'
    print 'request', cmd, address
    res=requests.post(url, json=payload, headers=headers).json()
    print 'response', cmd, address, res['result']['reply']

    #Wait for PWB to reboot
    print 'Wait for ', address, ' to reboot',
    start_time = time.time()
    elapsed_time = 0.
    timeout=300. # s = 5 min
    succ=False

    while elapsed_time <= timeout:
        if pwbping(address):
            print ' ready'
            succ=True
            break
        print '.',
        time.sleep(10)
        elapsed_time = time.time() - start_time

    print ''
    if succ:
        print 'reboot succesful'
        return 0
    else:
        print 'rebooting timeout'
        return 1

def uploadRPDfilePWBuserpage(ipwb, 
                             rpdfile,
                             newgithash):

    tool_up='esper-tool -v upload '
    tool_up_rpd=tool_up + ' -f %s '%rpdfile + ipwb + ' update'
    
    tool_w='esper-tool -v write '
    tool_w_selusr=tool_w + '-d 1 ' + ipwb + ' update' + ' image_selected'
    tool_w_reboot=tool_w + '-d 1 ' + ipwb + ' update' + ' reconfigure'

    tool_r='esper-tool -v read '
    tool_r_githash=tool_r+ipwb+' board git_hash'

    tool_r_imagesel=tool_r+ipwb+' update' + ' image_selected'

    # upload rpd file
    print 'Uploading file to user page...'
    dest=' file_rpd'
    print dest, rpdfile
    print 'next: ', tool_up_rpd+dest
    try:
        #out=sp.check_output(tool_up_rpd+dest,stderr=sp.STDOUT,shell=True)
        #print out.strip()
        sp.check_call(tool_up_rpd+dest,stderr=sp.STDOUT,shell=True)
    except sp.CalledProcessError as e:
        print 'Error raised in ', tool_up_rpd, e.output
        return 1
    print 'Upload done on ', ipwb

    '''    
    # select boot from user page
    print 'next: ', tool_w_selusr
    try:
        out=sp.check_output(tool_w_selusr,stderr=sp.STDOUT,shell=True)
        print out.strip()
    except sp.CalledProcessError as e:
        print 'Error raised in ', tool_w_selusr, e.output
        return 1
    # soft reboot
    print 'soft reboot'
    try:
        sp.call(tool_w_reboot,shell=True)
    except KeyboardInterrupt:
        print 'manual return'

    '''
    # hard reboot
    print 'hard reboot'
    stat=PWBreboot(ipwb)
    if stat:
        return 2

    # wait for pwb to reboot into user page
    print 'next: ', tool_r_imagesel
    img='0'
    att=0
    while True:
        if att > 5:
            break
        try:
            img=sp.check_output(tool_r_imagesel,stderr=sp.STDOUT,shell=True)
        except sp.CalledProcessError as e:
            print e.output, 'FAILED'
        if '1' in img:
            print img.strip(), ' ok'
            break
        else:
            print 'still in factory page'
        time.sleep(10)
        att+=1

    # read git hash, make sure is the one I uploaded
    print 'next: ', tool_r_githash
    try:
        gh=sp.check_output(tool_r_githash,stderr=sp.STDOUT,shell=True)
        print gh.strip()
    except sp.CalledProcessError as e:
        print e.output, 'FAILED'
        
    if newgithash in gh:
        print 'Excellent'


if __name__ == '__main__':

    if socket.gethostname() == 'alphagdaq.cern.ch':
        print 'Good! We are on', socket.gethostname()
    else:
        sys.exit('Wrong host %s'%socket.gethostname())

    print 'Running ', sys.argv[0]

    if len(sys.argv) == 2:
        uploadRPDfilePWBuserpage(sys.argv[1])
    elif len(sys.argv) == 4:
        uploadRPDfilePWBuserpage(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print "Need PWB address"
        print "Usage: updatePWBuserpage pwbXX"
        print "Usage: updatePWBuserpage pwbXX rpd_file git_hash"
        sys.exit()
