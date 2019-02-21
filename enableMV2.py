#!/usr/bin/python3

import pythonMidas
import socket
import sys
import subprocess as sp


def enableMV2():
    pwb_list=open('pwb_withMV2.list')
    for ipwb in pwb_list:
        print('Enabling MV2 on',ipwb)
        cmd='esper-tool -v write -d true ' + ipwb.strip() + ' board mv2_enable'
        try:
            sp.check_call(cmd,stderr=sp.STDOUT,shell=True)
        except sp.CalledProcessError as e:
            print('Error raised in ', cmd, e.output)
            return 1
    pwb_list.close()

# esper-tool -v write -d true pwb29 board mv2_enable

def enableMV2odb(sens,res):
    key='/Equipment/CTRL/Settings/PWB/modules'
    pwbs=pythonMidas.getString( key ).split()
    pwb_list=open('pwb_withMV2.list')
    for ipwb in pwb_list:
        ipwb = ipwb.strip()
        odb_index = pwbs.index(ipwb)

        print('Enabling MV2 on',ipwb,'at',odb_index)
        key='/Equipment/CTRL/Settings/PWB/mv2_enabled['
        key+=str(odb_index)
        key+=']'
        pythonMidas.setValue( key, 1 )

        print('Set MV2 range on',ipwb,'at',odb_index,'to',sens)
        key='/Equipment/CTRL/Settings/PWB/mv2_range['
        key+=str(odb_index)
        key+=']'
        pythonMidas.setValue( key, sens )

        print('Set MV2 resolution on',ipwb,'at',odb_index,'to',res)
        key='/Equipment/CTRL/Settings/PWB/mv2_resolution['
        key+=str(odb_index)
        key+=']'
        pythonMidas.setValue( key, res )

        
def setRangeMV2(sens):
    pwb_list=open('pwb_withMV2.list')
    for ipwb in pwb_list:
        print('Enabling MV2 on',ipwb)
        cmd='esper-tool -v write -d '+ str(sens) + ' ' + ipwb.strip() + ' board mv2_range'
        try:
            sp.check_call(cmd,stderr=sp.STDOUT,shell=True)
        except sp.CalledProcessError as e:
            print('Error raised in ', cmd, e.output)
            return 1
    pwb_list.close()




if __name__ == '__main__':

    if socket.gethostname() == 'alphagdaq.cern.ch':
        print('Good! We are on', socket.gethostname())
    else:
        sys.exit('Wrong host %s'%socket.gethostname())

    print('Running ', sys.argv[0])

    
    #enableMV2()
    sens=2
    res=3
    if len(sys.argv) > 1:
        sens = sys.argv[1]
    if len(sys.argv) > 2:
        sens = sys.argv[1]
        res =  sys.argv[2]
    #setRangeMV2(sens)
    
    enableMV2odb(sens,res)
