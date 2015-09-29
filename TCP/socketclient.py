__author__ = 'ugunipati'

import socket

host = '127.0.0.1'
port = 12345
n = 1


while n < 4:
    s = socket.socket()
    s.connect((host, port))
    print s.recv(1024)
    s.close()
    n += 1
