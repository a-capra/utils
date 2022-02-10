#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

def san(s):
    return float(s.strip('ms'))

df=pd.read_table('/home/agdaq/hotfs.log',sep=' ',names=('date','time','data','hist'),
                 parse_dates={'Datetime':[0,1]})
df['data']=df['data'].apply(san)
df['hist']=df['hist'].apply(san)


ax1=df.plot(x='Datetime',y=['data','hist'],yerr=3.,label=['data','history'],fmt='o',figsize=(16,11))
ax1.set(xlabel="", ylabel="Runtime [ms]")
ax1.grid(axis='y', linestyle='--', linewidth=2)
ax1.xaxis.label.set_size(20)
ax1.yaxis.label.set_size(20)
ax1.tick_params(labelsize='x-large')

fig=plt.gcf()
fig.tight_layout()
plt.savefig('ls_time_series.pdf')
plt.show()

