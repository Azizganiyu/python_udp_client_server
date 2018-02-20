# -*- coding: utf-8 -*-

from socket import *
def UDPServer():
    serverPort = 8080
    #serverName = 'hostname'
    serverSocket = socket(AF_INET ,SOCK_DGRAM)
    serverSocket.bind(('127.0.0.1', serverPort))
    print("The server is ready to receive")
    mssg, clientAddress = serverSocket.recvfrom(2048)
    mssg = mssg.decode().split(' ')
    option = int(mssg[0]) 
    var1 = int(mssg[1])
    var2 = int(mssg[2])
    def calculate(option,var1,var2):
        if (option == 1):
	        return var1 + var2
        elif (option == 2):
	        return var1 - var2
        elif (option == 3):
	        return var1 * var2
        elif (option == 4):
	        return var1 / var2
        elif (option == 5):
	        return var1 % var2
    while 1:
        result = str(calculate(option,var1,var2))
        serverSocket.sendto(result.encode('utf-8'), clientAddress)
        
    return
    
UDPServer ()