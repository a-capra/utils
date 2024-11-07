#!/usr/bin/env python

# packet to install:
# pip install pyserial
import serial

with serial.Serial('/dev/ttyUSB0',timeout=None) as s:
    print(s)
    print("Try write")
    s.write(str.encode('*IDN?'))
    print("Try read")
    print ('firmware:', s.read(10).decode())


