from sys import argv

mode='normal'

if len(argv) == 2:
	mode=argv[1]
elif len(argv) == 3:
	mode=argv[1]
	vv=float(argv[2])

if len(argv) < 3:
	vv=float(input("DMM reading in Volts "))

	
# normal mode: 1000 uA : 10 V = I : vv
# low current mode: 100 uA : 10 V = I : vv

if mode=='low':
	I = 10.*vv
	print("Current is %1.0f nA"%(I*1.e3))
else:
	I = 100.*vv
	print("Current is ",I,"uA")