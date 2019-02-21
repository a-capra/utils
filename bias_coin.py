# -*- coding: utf-8 -*-
"""
Created on Wed May 16 23:58:25 2018

@author: andrea

We would like to calculate how many flips of 2 coins, one biased and one fair,
we must observe to be 95% confident that the coin with more heads is the  
biased one.  
"""

import scipy.special

conf=0.95

#for prob in range(60,100,10):
#    p=prob*1.e-2
for p in [0.51,0.55,0.6,0.65,0.7,0.75,0.8,0.9,0.99]:
    n=1
    while True:
        q=0.
        for k in range(0,n+1):
            for j in range(0,k):
                q+=0.5**n*scipy.special.binom(n, k)*scipy.special.binom(n, j)*p**k*(1.-p)**(n-k)
        if q>=conf:
            print('{}\t{}\t{:.3f}'.format(p,n,q))
            break
        else:
            n+=1