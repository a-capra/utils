#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import speed_of_light

def gamma(v):
    #beta = np.divide(v,speed_of_light)
    beta = v/(speed_of_light*3.6)
    return 1./np.sqrt(1.-np.square(beta))

if __name__ == '__main__':

    with plt.xkcd():
        speed = np.linspace(0.,speed_of_light*3.6,1000)
        plt.plot(speed,gamma(speed))
        print(plt.xticks())
        plt.xticks([])
        plt.yticks([])
        plt.xlabel('speed in km/h')
        plt.ylabel('how much relativistic you are')
        plt.show()
