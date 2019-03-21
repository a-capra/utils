#!/usr/bin/env python3

import json
from pprint import pprint
import argparse
from sys import stdin
from os import environ
from pathlib import Path

def parse(dbname):
    with open(dbname) as f:
        data = json.load(f)
    return data

def trigger_src(data):
    src=data['Equipment']['CTRL']['Settings']['TrigSrc']
    tsrc=[]
    for s in src:
        if type(src[s]) == 'dict':
            continue
        if src[s] == True:
            tsrc.append(s)
    return tsrc

def SelectedFile(data):
    sel=data['Equipment']['CTRL']['Settings']['TRG']['MluSelectedFile']
    f=data['Equipment']['CTRL']['Settings']['TRG']['MluFiles'][int(sel)]
    return f,sel

def SelectedMult(data):
    mult=data['Equipment']['CTRL']['Settings']['TRG']['BscMultiplicity']
    if data['Equipment']['CTRL']['Settings']['TRG']['BscBotTopOr']:
        log='OR'
    elif data['Equipment']['CTRL']['Settings']['TRG']['BscBotTopAnd']:
        log='AND'
    else:
        log='Unknown'
    return mult,log

def PrintTrigConf(run):
    #path='/alpha/agdaq/data/'
    path1=environ['AGMIDASDATA']+'/'
    fname='run%05d.json'%int(run)
    if Path(path1+fname).is_file():
        path=path1
    elif Path('./'+fname).is_file():
        path='./'
    else:
        print("couldn't find",fname)
        return
    
    jsond=parse(path+fname)
    entry=trigger_src(jsond)
    #print(entry)
    print('Run',run)
    for src in entry:
        #print(src)
        if 'MLU' in src or 'mlu' in src:
            file_name,file_entry=SelectedFile(jsond)
            print(src,file_entry,'filename:',file_name,'\n')
        elif ('Bsc' in src or 'BSC' in src or 'bsc' in src) and ('mult' in src or 'Mult' in src):
            multiplicity,logic=SelectedMult(jsond)
            print(src,'Multiplicity:',multiplicity,'Logic:',logic)
        else:
            print(src,'\n')


if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Find out the trigger configuration for given run')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-r','--run', type=int,
                       nargs='*',
                       help='Run number')
    group.add_argument('-l','--runlist',
                       nargs='?',
                       type=argparse.FileType('r'),
                       default=stdin,
                       help='List of runs')
    
    args = parser.parse_args()

    if args.run == None:
        runlist=[r.strip() for r in args.runlist]
    else:
        runlist=args.run

    for r in runlist:
        PrintTrigConf(r)
