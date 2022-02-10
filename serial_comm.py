#!/usr/bin/env python

# packet to install:
# pip install pyserial
import serial

s=serial.Serial('/dev/ttyUSB0',timeout=1)
print s
s.write('x\r\n')
print 'firmware:', s.read(17).strip('\r\n')
s.write('d\r\n')
print s.read(17).strip('\r\n')
s.write('pow\r\n')
print s.read(17).strip('\r\n')
s.close()
