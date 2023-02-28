# UDPPingerClient.py
import time
from socket import *

# Set the server address and port number
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set a timeout value of 1 second
clientSocket.settimeout(1.0)

# Send 10 ping messages to the server
for i in range(10):
    # Get the current time in seconds since the epoch
    sendTime = time.time()

    # Construct the message to send
    message = 'Ping ' + str(i+1) + ' ' + str(sendTime)

    try:
        # Send the message to the server
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # Receive the server's response
        response, serverAddress = clientSocket.recvfrom(1024)

        # Get the current time again to calculate the RTT
        recvTime = time.time()

        try:
        # Extract the sequence number and server send time from the response message
            seqNum, serverSendTime = response.decode().split()

        # Calculate the round trip time (RTT) in seconds
            rtt = recvTime - sendTime

        # Print the response message and RTT
            print('Ping message', seqNum, 'received from', serverName)
            print('RTT:', rtt, 'seconds')
        except ValueError:
        # If the response message is not in the expected format, print the raw message
            print('Received message:', response.decode())
    except timeout:
        # If the response times out, print a message
        print('Request timed out')
    
# Close the socket
clientSocket.close()
