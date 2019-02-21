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

pprint(data)

