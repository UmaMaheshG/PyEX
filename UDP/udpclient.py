__author__ = 'ugunipati'


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('Hi Shashi', ('127.0.0.1', 5000))
s.close()


