# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:32:29 2019

@author: acapra
"""

from sympy import *
x = Symbol('x')
y = Symbol('y')
s = Symbol('s')

pprint(integrate(-s/(2*pi*(x**2+y**2+s**2)**(3/2)),y))
print "<----------------------------------------------->"
pprint(integrate(-s/(2*pi*(x**2+y**2+s**2)**(3/2)),(y,-oo,oo)))