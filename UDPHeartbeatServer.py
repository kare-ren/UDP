# UDPPingerServer.py
# We will need the following module to generate randomized lost packets import random
from socket import *
import random
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM) # Assign IP address and port number to socket serverSocket.bind((‘ ‘, 12000))
serverSocket.bind(('localhost', 12000))
messageNum = 0
checkTimeout = time.time()
checkForTimeout = False
while True:
    #fix for broken code given
    message, address = serverSocket.recvfrom(1024)
    message = message.decode()
    m = message.split()
    timeElapsed = time.time() - float(m[1])
    while(messageNum != int(m[0])):
        print("Packet #%d missed." % (int(messageNum) + 1))
        messageNum = messageNum + 1
    messageNum = messageNum + 1
    print("Packet #%s received in %f seconds." % (messageNum, timeElapsed))
    checkForTimeout = True
