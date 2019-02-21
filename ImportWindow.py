#!/usr/bin/env python

import time
import os
import os.path
import subprocess as sp

if __name__ == '__main__':

    #windowname='Cheese'
    windowname='"Take a Photo"'
    failed=0
    delay=1300
    try:
        while True:
            if delay < 61:
                imagename=os.environ['HOME']+'/andrea/O2test/'+time.strftime("%Y%b%d%H%M%S", time.localtime())+'.png'
            else:
                imagename=os.environ['HOME']+'/andrea/O2test/'+time.strftime("%Y%b%d%H%M", time.localtime())+'.png'

            cmd='import -window '+windowname+' '+imagename
            try:
                sp.check_output(cmd, stderr=sp.STDOUT, shell=True)
            except sp.CalledProcessError as e:
                print cmd, 'FAILED:', e.output
                failed=failed+1
                if failed < 100:
                    continue
                else:
                    break

            if os.path.isfile(imagename):
                print 'Image saved as ', imagename
            else:
                print 'Image NOT saved'
            print 'press CTRL+C to stop'
            # take a picture every 30 min
            time.sleep(delay)
            

    except KeyboardInterrupt:
        print 'interrupted!' 
