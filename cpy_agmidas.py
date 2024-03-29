#!/usr/bin/env python3

import paramiko
# https://github.com/jbardin/scp.py
from scp import SCPClient
import argparse
import sys
from pathlib import Path
from multiprocessing import Pool

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def progress(filename, size, sent):
    sys.stdout.write("%s progress: %.2f%%   \r" % (str(filename, 'utf-8'), float(sent)/float(size)*100) )

def progress4(filename, size, sent, peername):
    sys.stdout.write("(%s:%s) %s progress: %.2f%%   \r" % (peername[0], peername[1], str(filename, 'utf-8'), float(sent)/float(size)*100) )

def getsubruns(runlist):
    filelist=[]
    for line in runlist:
        run=int(line.strip())
        sub=0
        subrun='/alpha/agdaq/data/run%05dsub%03d.mid.lz4'%(run,sub)
        subfile=Path(subrun)
        while subfile.is_file():
            filelist.append(subrun)
            sub+=1
            subrun='/alpha/agdaq/data/run%05dsub%03d.mid.lz4'%(run,sub)
            subfile=Path(subrun)
    return filelist

def getnewsubruns(runlist):
    filelist=[]
    localpath='/daq/alpha_data0/acapra/alphag/midasdata/'
    remotepath='/eos/experiment/ALPHAg/midasdata_old/'
    for line in runlist:
        l=line.split()
        subrun=str(l[0].strip())
        subsize=int(l[1].strip())
        subfile=Path(subrun)
        localfile=Path(localpath+subfile.parts[-1])
        if localfile.is_file():
            #print(f'yes {subrun}')
            localsize=int(localfile.stat().st_size)
            if localsize==subsize:
                continue
        #print(f'no {subrun}')
        filelist.append(remotepath+subrun)
    return filelist

def worker(runfile):
    server='lxplus.cern.ch'
    port=22
    user='acapra'
    password='password'
    
    ssh = createSSHClient(server, port, user, password)
    scp = SCPClient(ssh.get_transport(), progress4=progress4)
    #scp = SCPClient(ssh.get_transport(), socket_timeout=None, progress=progress)
    dst='/daq/alpha_data0/acapra/alphag/midasdata'
    try:
        scp.put(runfile.strip(),remote_path=dst)
    except FileNotFoundError:
        print(f'{runfile} not found')

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='copy ALPHA-g MIDASfiles to my workspace')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='List of runs')
    args = parser.parse_args()

    #server='lxplus.cern.ch'
    server='alpha00.triumf.ca'
    port=22
    user='acapra'
    password='password'
    
    ssh = createSSHClient(server, port, user, password)
    #scp = SCPClient(ssh.get_transport(), progress4=progress4)
    scp = SCPClient(ssh.get_transport(), socket_timeout=None, progress=progress)

    src=getsubruns(args.infile)
    #src=getnewsubruns(args.infile)
    #for f in src:
    #    print(f)
            
    #dst='/afs/cern.ch/user/a/acapra/workspace/agdata'
    dst='/daq/alpha_data0/acapra/alphag/midasdata'

    print('Ready for transfer')

    # recursive for directories
    # scp.put(src, recursive=True, remote_path=dst)
    #
    scp.put(src, remote_path=dst)

    #pool = Pool(processes=5)
    #pool.map(worker, src)


