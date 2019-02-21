# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:57:25 2018

@author: andrea
"""

import numpy as np
import matplotlib.pyplot as plt

fname='C:/Users/andrea/Documents/ALPHA-g/DAQ_clock_pics/C1Trace00000.txt'
t,V = np.loadtxt(fname,delimiter=',',skiprows=5,unpack=True)

plt.plot(t,V)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [V]')
