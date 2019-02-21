# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:19:52 2017

@author: andrea
"""

import numpy as np
from scipy.stats import norm
from scipy.stats import cauchy
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 1)

x = np.linspace(-10,10,1000)

ax.plot(x, norm.pdf(x), 'r-', lw=5, alpha=0.6, label='norm pdf')
ax.plot(x, cauchy.pdf(x), 'b-', lw=5, alpha=0.6, label='cauchy pdf')
ax.legend(loc='best', frameon=False)
plt.show()