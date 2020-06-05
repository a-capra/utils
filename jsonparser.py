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

while True:
    for i in data:
        if i[0] == '/':
            continue
        print(i)
    print('------------------------------')
    
    check_key=True
    while check_key:
        try:
            s = input('Choose one: ')
        except EOFError:
            exit(0)
        try:
            data[s]
            check_key=False
        except KeyError:
            print(s,'is not recognized')

    if isinstance(data[s], dict):
        data=data[s]
    else:
        print(data[s])
        break


