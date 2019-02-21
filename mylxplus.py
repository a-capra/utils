#!/usr/bin/env python3

import sys, paramiko

hostname='lxplus.cern.ch'
port=22
username='acapra'
password='Chang*Passwd1Year'

command='xterm'

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)    
    
    client.connect(hostname, port=port, username=username, password=password)

    chan = client.invoke_shell()
    chan.settimeout(None)

    #chan.close()

finally:
    client.close()
