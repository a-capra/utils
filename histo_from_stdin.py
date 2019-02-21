#!/usr/bin/env python3

import sys
import argparse
import shutil

def show(histo,mod=1,srt=True):
    if srt:
        kkk=sorted(histo.keys())
    else:
        kkk=histo.keys()
    for k in kkk:
        out=k+' '
        N=int(histo[k]*mod)
        for i in range(N):
            out+='*'
        if N>0:
            out+=' '
        out+= str(histo[k])
        print(out)
         
if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-f','--fitscreen', help='fit histogram into terminal width',
                        action='store_true')
    parser.add_argument('-u','--unsort', help='unsorted labels',
                        action='store_false')
    
    args = parser.parse_args()
    
    data=[line.strip() for line in args.infile]
    histo=dict((x, data.count(x)) for x in data)

    if args.fitscreen:
        dmax=max(histo.values())
        lmax=max([len(str(k)) for k in histo.keys()])
        ymax=shutil.get_terminal_size().columns - lmax - len(str(dmax)) - 2
        norm=ymax/dmax
    else:
        norm=1

    show(histo,norm,args.unsort)


    
    '''
    for k in sorted(histo):
        out=k+' '
        for i in range(histo[k]):
            out+='*'
        print(out, histo[k])
    '''
