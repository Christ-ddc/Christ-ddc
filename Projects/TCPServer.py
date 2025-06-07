#!/usr/bin/python3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.57.4'
host = socket.gethostname()
port = 444

#Binding to socket
serversocket.bind((host, port)) #Host will be replaced/substituted with IP, if changed and not running on host

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()

    print("Received connection from " % str(address))

    message = 'Hello! Thank you for connecting to the server' + "\r\n"

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()