__author__ = 'ugunipati'

import socket


try:

    UDP_SERVER_SOCKET = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    UDP_SERVER_SOCKET.bind(('127.0.0.1', 5000))
    print"UDPServer Waiting for client on port 5000"
    while 1:
        data, address = UDP_SERVER_SOCKET.recvfrom(256)
        print "( ", address[0], " ", address[1], " ) said : ", data
except IOError:
    print 'Error:Not able to connect to the Server',IOError.message


