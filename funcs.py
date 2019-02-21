# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:00:32 2017

@author: andrea
"""

from math import exp
import numpy as np
import matplotlib.pyplot as plt


def gauss(x,a,b,c):
    return a*exp(-(x-b)**2/(2*c**2))

def lorentz(x,a,b,c):
    return a*c/((x-b)**2+(0.5*c)**2)

def lorgaus(x,A,x0,s,w):
    return A*(exp(-(x-x0)**2/(2*s**2))+(w/((x-x0)**2+(0.5*w)**2)))

amp = 1.
mean = 0.
sigma = 1.
width = 1.

xmin = -5.
xmax = -xmin

x = np.linspace(xmin,xmax,1000)
y1 = np.vectorize(gauss)
y2 = np.vectorize(lorentz)
y3 = np.vectorize(lorgaus)

fig, ax = plt.subplots(1, 1)
fig.set_figwidth(10)
fig.set_figheight(9)
ax.plot(x, y1(x,amp,mean,sigma), 'r-', lw=5, alpha=0.6, label='Gauss')
ax.plot(x, y2(x,amp,mean,width), 'b-', lw=5, alpha=0.6, label='Lorentz')
ax.plot(x, y1(x,amp,mean,sigma)+y2(x,amp,mean,width), 'k-', lw=5, alpha=0.6, label='Gauss+Lorentz')
ax.plot(x, y3(x,amp,mean,sigma,width), 'g-', lw=5, alpha=0.6, label='Gauss+Lorentz')
ax.legend(loc='best', frameon=False)
plt.show()
