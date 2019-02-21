#!/usr/bin/python3

fin=open('runlog.temp')
fout=open('writterun.txt','w')
for l in fin:
    if 'Written' in l:
        #print(l.strip())
        fout.write(l.strip()+'\n')
    elif l=='':
        continue
fin.close()
fout.close()


lines=open('writterun.txt').readlines()
fout=open('writterunsorted.txt','w')
for line in sorted(lines, key=lambda line: int(line.split()[6]),reverse=True):
    fout.write(line)
fout.close()
