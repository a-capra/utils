#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from os import environ
from pathlib import Path
from sys import exit

def san(s):
    return float(s.strip('ms'))

fin = Path(f"{environ['HOME']}/hotfs.log")
#fin = Path("./hotfs.log")
if fin.is_file():
    print(f"Reading {fin.as_posix()}")
else:
    print(f"{fin.as_posix()} does not exists")
    exit()
    
df = pd.read_table(f'{fin.as_posix()}',delim_whitespace=True,names=('date','time','data','hist'),parse_dates={'Datetime':[0,1]},date_format='%d-%m-%Y %H:%M:%S')
df['data'] = df['data'].apply(san)
df['hist'] = df['hist'].apply(san)


ax1 = df.plot(x='Datetime',y=['data','hist'],yerr=3.,label=['data','history'],fmt='o',figsize=(16,11))
ax1.set(xlabel="", ylabel="Runtime [ms]")
ax1.grid(axis='y', linestyle='--', linewidth=2)
ax1.xaxis.label.set_size(20)
ax1.yaxis.label.set_size(20)
ax1.tick_params(labelsize='x-large')

fig = plt.gcf()
fig.tight_layout()
plt.savefig('ls_time_series.pdf')
plt.show()

