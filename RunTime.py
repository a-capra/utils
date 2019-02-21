#!/usr/bin/env python3

import json
from datetime import datetime
import argparse
from sys import stdin

def parse(dbname):
    with open(dbname) as f:
        data = json.load(f)
    return data

def PrintRunTime(run):
    print('Run:',run)
    path='/alpha/agdaq/data/'
    fname='run%05d.json'%int(run)
    
    jsond=parse(path+fname)
    start_time=jsond['Runinfo']['Start time']
    print('Start:',start_time)
    stop_time=jsond['Runinfo']['Stop time']
    print('Stop:',stop_time)

    duration=int(jsond['Runinfo']['Stop time binary'],base=16)-int(jsond['Runinfo']['Start time binary'],base=16)
    print('Duration:',duration,'s')
    '''
    print(datetime.fromtimestamp(int(jsond['Runinfo']['Start time binary'],base=16)).strftime('%c'))
    print(datetime.fromtimestamp(int(jsond['Runinfo']['Stop time binary'],base=16)).strftime('%c'))

    startts=datetime.strptime(start_time,'%c')
    stoptts=datetime.strptime(stop_time,'%c')
    print('Duration:',(stoptts-startts).total_seconds(),'s')
    '''
    
if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Find out the duration of a given run')
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
        PrintRunTime(r)
