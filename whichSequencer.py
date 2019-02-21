#!/usr/bin/env python3

from sys import argv,exit
import json
from pprint import pprint


if len(argv) == 2:
    dbname=argv[1]
else:
    print('Usage:\t %s odbname.json'%argv[0])
    exit(1)

with open(dbname) as f:
    data = json.load(f)

#pprint(data)

key1="Equipment"
#key2="sequencerA"
#pprint(data[key1][key2])
key3A="Common"
key3AA="Status"
#print(str(data[key1][key2][key3A][key3AA]))
key3AB="Event ID"
#print(int(data[key1][key2][key3A][key3AB],0))

key3B="Settings"
key3BA="tcp_port"
#print(int(data[key1][key2][key3B][key3BA],16))

for key2 in ["sequencerA","sequencerB","sequencerC","SequencerD"]:
    print(str(data[key1][key2][key3A][key3AA]))
    print("Event ID: ",int(data[key1][key2][key3A][key3AB],0))
    print("TCP port: ",int(data[key1][key2][key3B][key3BA],16),"\n")
