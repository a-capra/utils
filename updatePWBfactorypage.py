#!/usr/bin/env python

import socket
import sys
import os
import requests
import json
import pythonMidas
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


# def updatePWBfactorypage(ipwb, rpdfile=os.environ['HOME']+'/online/firmware/pwb_rev1/feam-2018-03-21-bootloader/feam_rev1_auto.rpd', newgithash='a0d50f0a3456b0898c0915bd905b1c5954835dc2'):
def updatePWBfactorypage(ipwb, rpdfile=os.environ['HOME']+'/online/firmware/pwb_rev1/pwb_rev1_20180531_cabf9d3d_bryerton/feam_rev1_auto.rpd', newgithash='cabf9d3d26a24ab44ffdbfc300059276eece46fe'):

    tool_up='esper-tool -v upload '
    tool_up_rpd=tool_up + ' -f %s '%rpdfile + ipwb + ' update'
    tool_w='esper-tool -v write '
    tool_w_selusr=tool_w + '-d 1 ' + ipwb + ' update' + ' image_selected'
    tool_w_selfac=tool_w + '-d 0 ' + ipwb + ' update' + ' image_selected'
    tool_r='esper-tool -v read '
    tool_r_githash=tool_r+ipwb+' board git_hash'


    print "test:", tool_r + ipwb + ' update' + ' image_selected'
    try:
        out=sp.check_output(tool_r + ipwb + ' update' + ' image_selected', stderr=sp.STDOUT, shell=True)
        print out.strip()
    except sp.CalledProcessError as e:
        print ipwb, 'error image_selected unknown'
        print 'try sel_page'
        tool_w_selusr=tool_w + '-d 0x1000000 ' + ipwb + ' update' + ' sel_page' # sel_page uses memory address instead of array index
    
    for attempt in range(3):

        # upload rpd file
        print 'Uploading file to user page... attempt #', attempt+1
        dest=' file_rpd'
        print dest, rpdfile
        print 'next: ', tool_up_rpd+dest
        try:
            out=sp.check_output(tool_up_rpd+dest,stderr=sp.STDOUT,shell=True)
            print out.strip()
        except sp.CalledProcessError as e:
            print 'Error raised in ', tool_up_rpd, e.output
            return 1
        print 'Upload done on ', ipwb

        # select boot from user page
        print 'next: ', tool_w_selusr
        try:
            out=sp.check_output(tool_w_selusr,stderr=sp.STDOUT,shell=True)
            print out.strip()
        except sp.CalledProcessError as e:
            print 'Error raised in ', tool_w_selusr, e.output
            return 1

        # pwb hard reboot and wait
        print ipwb, 'REBOOT'
        stat=PWBreboot(ipwb)
        if stat:
            return 2

        # read git hash, make sure is the one I uploaded
        print 'next: ', tool_r_githash
        gh='0'
        try:
            gh=sp.check_output(tool_r_githash,stderr=sp.STDOUT,shell=True)
            print gh
        except sp.CalledProcessError as e:
            print e.output, 'FAILED'
            continue
        if newgithash in gh:
            break


    print '\nUploading file to factory page'

    tool_w_factw=tool_w + ' -d true ' + ipwb + ' update ' + ' allow_factory_write'
    print 'next: ', tool_w_factw
    try:
        out=sp.check_output(tool_w_factw,stderr=sp.STDOUT,shell=True)
        print out.strip()
    except sp.CalledProcessError as e:
        print 'Error raised in ', tool_w_factw, e.output
        return 1

    dest=' factory_rpd'
    print dest, rpdfile
    print 'next: ', tool_up_rpd+dest
    try:
        out=sp.check_output(tool_up_rpd+dest,stderr=sp.STDOUT,shell=True)
        print out.strip()
    except sp.CalledProcessError as e:
        print 'Error raised in ', tool_up_rpd, e.output
        return 1

    # select boot from factory page
    print 'next: ', tool_w_selfac
    try:
        out=sp.check_output(tool_w_selfac,stderr=sp.STDOUT,shell=True)
        print out.strip()
    except sp.CalledProcessError as e:
        print 'Error raised in ', tool_w_selfac, e.output
        return 1

    # pwb hard reboot and wait
    print ipwb, 'REBOOT'
    stat=PWBreboot(ipwb);
    if stat:
            return 3

    print 'next: ', tool_r_githash
    gh=sp.check_output(tool_r_githash,stderr=sp.STDOUT,shell=True)
    print 'firmware for', ipwb, 'is', gh
    return 0



if __name__ == '__main__':

    if socket.gethostname() == 'alphagdaq.triumf.ca':
        print 'Good! We are on', socket.gethostname()
    else:
        sys.exit('Wrong host %s'%socket.gethostname())

    if len(sys.argv) == 2:
        updatePWBfactorypage(sys.argv[1])
    elif len(sys.argv) == 4:
        updatePWBfactorypage(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print "Need PWB address"
        print "Usage: updatePWBfactorypage pwbXX"
        print "Usage: updatePWBfactorypage pwbXX rpd_file git_hash"
        sys.exit()
