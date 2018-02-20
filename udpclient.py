from socket import *

def udp_client():
    serverName = '127.0.0.1'
    serverPort =  8080
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    print('Select Operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulus \n')
    option = input('\nchoose your option\n')
    var1 = input ('\nEnter first variable\n')
    var2 = input ('\nEnter second variable\n')
    mssg = option+' '+var1+' '+var2 
    clientSocket.sendto(mssg.encode('utf-8'),(serverName, serverPort))
    result, serverAddress = clientSocket.recvfrom(2048)
   
    print (result)
    clientSocket.close()

    return

udp_client()

wait = input('\nEnter any key to close\n')