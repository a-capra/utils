#!/usr/bin/python3

from sys import argv
from os import environ
from random import uniform

fname=[environ['HOME']+'/utils/quotes.txt',environ['HOME']+'/utils/quotes2.txt']
idx=0
if len(argv) == 2:
    idx=argv[1]

with open(fname[idx]) as f:
    data = f.readlines()
    l=int(uniform(0,len(data)))

    if idx == 0:
        q=data[l].split(';')
    else:
        q=data[l].split('~')

    print(q[0].strip(),'\n\t',q[1].strip())
