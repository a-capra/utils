#!/usr/bin/env python

#Socket client example in python
 
import socket   #for sockets
import sys      #for exit
 
def pwbping(host):

#create an INET, STREAMing socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print 'Failed to create socket'
        #sys.exit()
        return False
     
    #print 'Socket Created'
    #host = 'pwb15'
    port = 80
 
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        #could not resolve
        print 'Hostname could not be resolved. Exiting'
        #sys.exit()
        return False

        print remote_ip

    #Connect to remote server
    try:
        s.connect((remote_ip , port))
        print 'Socket Connected to ' + host + ' on ip ' + remote_ip
    except socket.error:
        print host, ': No route to host'
        #sys.exit()
        return False

    #Send some data to remote server
    message = "GET / HTTP/1.1\r\n\r\n"
    try:
        #Set the whole string
        s.sendall(message)
    except socket.error:
        #Send failed
        print 'Send failed'
        #sys.exit()
        return False
    
    print 'Message send successfully'

    #Now receive data
    reply = s.recv(len(message)-1).strip()
    print reply
    return '200 OK' in reply

if __name__ == '__main__':
    inpwb='pwb12'
    if len(sys.argv) == 2:
        inpwb=sys.argv[1]
    if pwbping(inpwb):
        print 'OK'
    else:
        print 'not OK'
