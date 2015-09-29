__author__ = 'ugunipati'

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 12345
BUFFER_SIZE = 20

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((TCP_IP, TCP_PORT))
serverSocket.listen(5)

while 1:
    c,a = serverSocket.accept()
    print 'Got connnection from', a
    c.send('Thank you connecting')
    c.close()










