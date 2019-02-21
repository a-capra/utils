#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from  collections import OrderedDict

import pythonMidas
key='/Equipment/CTRL/Settings/PWB/modules'
pwbs=pythonMidas.getString( key ).split()
loc={}
for ipwb in pwbs:
    i=pwbs.index(ipwb)
    col=int(i/8)
    ring=i%8
    loc[ipwb]=[col,ring]

tag='2018May161804'
dirname='./PCPWB'+tag
#fff='./PCPWB2018Apr141616/cycle001.log'
fff='%s/cycle001.log'%dirname
pwbs,s=np.loadtxt(fff,dtype=str, delimiter='\t', unpack=True)
cnt={} # failure by address
for ipwb in pwbs:
    cnt[ipwb]=0

ccf=[0]*8 # failure by column

Ncycles=100
ccc=[0]*Ncycles # failure by cycle

for cycle in range(1,1+Ncycles):
    #filename='./PCPWB2018Apr141616/cycle%03d.log'%cycle
    #filename='./PCPWB2018Apr161104/cycle%03d.log'%cycle
    #filename='./PCPWB2018Apr161246/cycle%03d.log'%cycl
    filename='%s/cycle%03d.log'%(dirname,cycle)
    name,stat=np.loadtxt(filename,dtype=str, delimiter='\t', unpack=True)
    d=dict(zip(name, stat))
    for p in d.keys():
        if d[p]=='3':
            cnt[p]+=1 # failure by address
            ccf[loc[p][0]]+=1 # failure by column
            ccc[cycle-1]+=1 # failure by cycle


#print cnt
print ''
cnto=OrderedDict(sorted(cnt.items()))
print cnto

centers = range(len(cnto))
fig1=plt.figure(1,figsize=(30, 10),facecolor='w')
fig1.canvas.set_window_title('power_cycle_test_by_address_'+tag)
plt.title('PWBs Failed to Boot in %d Power Cycles. firmware: 536ace9f4b39f34a51c6b2055da6d4ab400f3c5a'%Ncycles,fontsize=18)
plt.bar(centers, cnto.values(), width=1)
plt.xticks(centers, cnto.keys(), rotation=45, fontsize=16)
plt.yticks(range(0,Ncycles+1,5))
plt.xlim([0, len(pwbs)])
plt.ylim([0, Ncycles+1])
plt.grid(axis='y')
fig1.tight_layout()

fig2=plt.figure(2,figsize=(30, 10),facecolor='w')
fig2.canvas.set_window_title('power_cycle_test_by_column_'+tag)
plt.title('Columns with PWBs Failed to Boot in %d Power Cycles. firmware: 536ace9f4b39f34a51c6b2055da6d4ab400f3c5a'%Ncycles,fontsize=18)
plt.bar(range(8),ccf,align='center',width=1)
plt.xticks(fontsize=16)
plt.xlabel('column #',fontsize=16)
#plt.yticks(range(0,Ncycles+1,5))
#plt.yticks(range(0,13,3))
plt.yticks(range(0,max(ccf)+1,3))
plt.xlim([-0.5, 7.5])
#plt.ylim([0, Ncycles+1])
#plt.ylim([0, 13])
plt.ylim([0, max(ccf)+1])
plt.grid(axis='y')
fig2.tight_layout()

fig3=plt.figure(3,figsize=(30, 10),facecolor='w')
fig3.canvas.set_window_title('power_cycle_test_by_cycle_'+tag)
plt.title('Cycles with PWBs Failed to Boot. firmware: 536ace9f4b39f34a51c6b2055da6d4ab400f3c5a',fontsize=18)
plt.bar(range(1,Ncycles+1),ccc,align='center',width=1)
plt.xticks(range(1,Ncycles+1,1),fontsize=13)
plt.xlabel('cycle #',fontsize=16)
#plt.yticks(range(0,64,1))
plt.yticks(range(0,max(ccc)+1,1))
plt.xlim([0, Ncycles+1])
#plt.ylim([0, 4])
plt.ylim([0, max(ccc)+1])
plt.grid()
fig3.tight_layout()


for ip in cnto.keys():
    if cnto[ip]>0:
        print 'addr:', ip, 'col:', loc[ip][0], 'failed:', cnto[ip]

plt.show()
