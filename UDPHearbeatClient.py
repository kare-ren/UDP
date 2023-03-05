# UDPPingerClient.py
import time
from socket import *
import threading

# Set the server address and port number
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set a timeout value of 1 second
clientSocket.settimeout(1.0)

messageNum = 0

while(True):
    sendTime = time.time()
    message = str(messageNum) + " " + str(sendTime)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    messageNum = messageNum + 1


# Close the socket
clientSocket.close()
