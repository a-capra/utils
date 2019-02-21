#!/usr/bin/env python

from sys import argv
from scipy.constants import m_e, e, pi

f=28.e9 # Hz, default value
try:
    f=float(argv[1])
except IndexError:
    print 'Cyclotron frequency in Hz required'

print f, 'Hz'
B=2.*pi*m_e*f/e
#print B, 'T = ', B*1.e4, 'G'
print 'B = %1.3e T = %1.2f G' % (B,B*1.e4)
