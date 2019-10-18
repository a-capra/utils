#!/usr/bin/env python3

from sys import argv,exit
import json
from pprint import pprint


if len(argv) == 2:
    dbname=argv[1]
else:
    print('Usage:\t %s file_name.json'%argv[0])
    exit(1)

with open(dbname) as f:
    data = json.load(f)

#pprint(data)
#print(data['Equipment']['TDC']['Common']['Frontend file name'])
#print(data['Equipment']['BVlvtop']['Settings'])
#print(data['Equipment']['BVlvbot']['Settings'])

while True:
    for i in data:
        if i[0] == '/':
            continue
        print(i)
    print('------------------------------')
    s = input('Choose one: ')
#    print(type(data))
    if isinstance(data[s], dict):
        data=data[s]
    else:
        print(data[s])
        break


