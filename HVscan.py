#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

V,I,R = np.loadtxt('HVscan.txt',delimiter='\t',skiprows=1,unpack=True)
plt.subplot(211)
plt.title('AW Voltage Vs AW Current')
plt.plot(V,I,'bo',label='current [nA]')
plt.ylim(0.0,max(I)*1.1)
plt.ylabel('curent [nA]')
plt.grid(True)

plt.subplot(212)
plt.title('AW Voltage Vs ADC-32 Grand-Or')
plt.plot(V,R,'ro',label='adc32-grand-or [Hz]')
plt.ylabel('adc32-grand-or [Hz]')
plt.xlabel('AW Voltage [V]')
plt.grid(True)

#plt.legend(loc='best')
fig=plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.tight_layout()
plt.show()
