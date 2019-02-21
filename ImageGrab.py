#!/usr/bin/env python

#import numpy as np
#import matplotlib.pyplot as plt
import pyscreenshot as ImageGrab
#from PIL import ImageGrab
import time
import os
if __name__ == '__main__':

    while True:
        # grab fullscreen
        img = ImageGrab.grab()
        
        #plt.imshow(img, cmap='gray', interpolation='bicubic')
        #plt.show()
        
        imagename=os.environ['HOME']+'/andrea/O2test'+time.strftime("%Y%b%d%H%M", time.localtime())+'.png'
        
        # save image file
        img.save(imagename)
        
        # show image in a window
        img.show()

        # take a picture every 30 min
        time.sleep(1300)
