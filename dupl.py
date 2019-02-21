#!/usr/bin/python3

import filecmp 
from sys import argv,exit
from os import listdir, environ, remove
from os.path import isfile, isdir, join, getsize
from itertools import combinations
from humanize import naturalsize

def generate_list_of_files(directory):
    flist=[]
    for f in listdir(directory):
        the_path = join(directory, f)
        if isfile(the_path):
            flist.append(the_path)
        elif isdir(the_path):
            flist.extend( generate_list_of_files(the_path) )
    return flist

def find_duplicates(files=None,max_size=10000000,stats=True):
    dupl=[]
    bigfiles=[]
    dupl_size=0
    for f1,f2 in combinations( files, 2 ):
        file_size=getsize(f1)
        if file_size > max_size:
            bigfiles.append((f1,f2))
            continue
        if filecmp.cmp(f1, f2):
            print(f1,'and',f2,'are identical')
            dupl.append((f1,f2))
            dupl_size+=file_size

    if stats:
        print('***** STATS *****')
        print('checked files:',len(files))
        print('skipped (size>'+str(naturalsize(max_size))+'):',len(bigfiles))
        print('identical files:',len(dupl))
        print('space allocated for duplicated files:',naturalsize(dupl_size))
        print('**********************')

    return dupl

def remove_duplicates(dupl):
    print('Please answer "0" or "1" to select the approriate file, or "2" for neither')
    cnt=0
    for f in dupl:
        code=-1
        while code not in range(3):
            ans=input('Remove 0) '+f[0]+' 1) '+f[1]+' or 2) neither? ')
            if ans == '':
                code=2
            else:
                code=int(ans)
        if code < len(f) and code >= 0:
            print('Ok, removing',f[code])
            remove(f[code])
            cnt+=1
    return cnt


if __name__=='__main__':

    if len(argv)==1:
        somedir=environ['HOME']
    else:
        somedir=argv[1]

    if isfile(somedir):
        print(somedir,'is a file')
        exit(1)
    else:
        files = generate_list_of_files( somedir )
        #print(files)

    dupl=find_duplicates( files )

    ans=input('Do you want to proceed with deletion? [y/N] ')
    files_removed = 0
    if ans.lower() == 'yes' or ans.lower() == 'y':
        files_removed = remove_duplicates(dupl)
    print('Number of files removed: ',files_removed)
