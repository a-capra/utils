#!/usr/bin/env python3


import os

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import dates as mpl_dates

from datetime import datetime, timedelta

from collections import deque
import numpy as np

class CPUtempMon:
    def __init__(self):
        '''
        Monitor CPU temperature of Raspberry Pi 3B+
        '''
       
        self.poll = 2160 # ms

        self.nsamples = 5000
        self.x = deque([],maxlen=self.nsamples)
        self.y = deque([],maxlen=self.nsamples)

        plt.style.use('fivethirtyeight')
        self.fig = plt.figure(figsize=(13,6))
        self.fig.canvas.manager.set_window_title('CPU temperature Monitor')
        self.ax1 = self.fig.add_subplot(1,1,1)
        
        self.date_format = mpl_dates.DateFormatter('%H:%M:%S')
        self.ax1.xaxis.set_major_formatter(self.date_format)
        self.ax1.xaxis.set_tick_params(labelsize='small')
        self.ax1.set_ylabel('Celsius', fontsize='medium')

        self.verb=True

    def set_verbose(self,val):
        self.verb=val

    def set_number_points(self,val):
        '''
        set number of points on the plot at any given time
        '''
        self.nsamples = int(val)
        self.x.maxlen=self.nsamples
        self.y.maxlen=self.nsamples

    def set_poll(self,val):
        '''
        set refreshing period, to be called before plot
        '''
        self.poll = val

    def animate(self,i):
        '''
        Update temperature plot        
        '''
        time = datetime.now()
        temp = self.get_cpu_temp()

        if self.verb:
            print(f'{i:7d} CPU temperature is {temp:.2f} Celsius at {time:%Y-%m-%d %H:%M:%S}') 

        self.x.append(time)
        self.y.append(temp)

        plt.cla()
        self.ax1.xaxis.set_major_formatter(self.date_format)
        self.ax1.plot(np.array(self.x),np.array(self.y),'-k')

    def get_cpu_temp(self):
        """
        Obtains the current value of the CPU temperature.
        :returns: Current value of the CPU temperature if successful, zero value otherwise.
        :rtype: float
        """
        # Initialize the result.
        result = 0.0
        # The first line in this file holds the CPU temperature as an integer times 1000.
        # Read the first line and remove the newline character at the end of the string.
        if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
            with open('/sys/class/thermal/thermal_zone0/temp') as f:
                line = f.readline().strip()
                # Test if the string is an integer as expected.
            if line.isdigit():
                # Convert the string with the CPU temperature to a float in degrees Celsius.
                result = float(line) / 1000
        # Give the result back to the caller.
        return result

    def plot(self):

        print(f'displaying {self.poll*self.nsamples*1.e-3} seconds')
        
        a=animation.FuncAnimation(self.fig, self.animate, interval=self.poll)

        plt.tight_layout()
        plt.show()

        return a

        
def main():

    monitor = CPUtempMon()
    #monitor.set_verbose(False)
    monitor.plot()

  
    

if __name__ == "__main__":
    main()
