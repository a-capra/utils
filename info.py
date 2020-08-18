from __future__ import print_function  # for Python2
import datetime
# To Get information about CPU, RAM, disk
import psutil
# To Get IP Address 
import socket

import sys
import os
p=sys.platform
if 'win' in p: os.system('cls')
else: os.system('clear')

hostname = socket.gethostname() 
IPAddr = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IPAddr = s.getsockname()[0]
s.close()
#
print("Your Computer Name is: " + hostname) 
print("Your Computer IP Address is: " + IPAddr) 

now = datetime.datetime.now()
print("Current date and time: ")
#print(str(now))
print(now.strftime('%H:%M:%S on %A, %d %B %Y'))


obj_Disk = psutil.disk_usage('/')

print('Total Disk size: {0:.3f} Gb'.format(obj_Disk.total / (1024.0 ** 3)))
print('Used Disk size: {0:.3f} Gb'.format(obj_Disk.used / (1024.0 ** 3)))
print('Free Disk size: {0:.3f} Gb'.format(obj_Disk.free / (1024.0 ** 3)))
print('Disk Fraction Used: {0:.0f}%'.format(obj_Disk.percent))

print('CPU usage:',psutil.cpu_percent(),'%')
#print(psutil.virtual_memory())  # physical memory usage
print('Memory usage:', psutil.virtual_memory()[2],'%')

