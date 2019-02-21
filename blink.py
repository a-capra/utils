import time
from sys import argv

def blink(msg,duty=0.5,duration=1):
    blank=''.join([' ' for c in msg])
    on=duration*duty
    off=duration*(1-duty)
    while True:
        try:
            print(msg,end='\r')
            time.sleep(on)
            print(blank,end='\r')
            time.sleep(off)
        except KeyboardInterrupt:
            break

if __name__=='__main__':

    print('say "ciao" every 2 seconds and t 70% duty cycle')
    print('quit with Ctrl+C\n')
    blink('CIAO!',0.7,2)
