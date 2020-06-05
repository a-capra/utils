#!/usr/bin/env python

flist=['/daq/alpha_data0/acapra/alphag/ping.txt',
'/daq/alpha_data0/acapra/alphag/midasdata/ping.txt',
'/daq/alpha_data0/acapra/alphag/MCdata/ping.txt']

for fname in flist:
  f=open(fname,"w")
  for i in range(200):
    #f.write("This is line %d\r\n" % (i+1))
    f.write("xxxx\n")
  f.close()
