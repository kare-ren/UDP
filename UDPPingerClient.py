# UDPPingerClient.py
import time
from socket import *

# Prints Round Trip Time and Packet Loss Statistics
def statistics(RTT, lost_packets):
    print('\nStatistics Summary:')

    minimum = min(RTT)
    print('Minimum RTT:', minimum, 'seconds')    

    maximum = max(RTT)
    print('Maximum RTT:', maximum, 'seconds')

    average = sum(RTT)/len(RTT)
    print('Average RTT:', average, 'seconds')

    packet_loss = lost_packets/10*100
    print('Packet Loss Rate:', packet_loss, '%')

    return


RTT = []
lost_packets = 0

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
        print('Send:', message)
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # Receive the server's response
        response, serverAddress = clientSocket.recvfrom(1024)

        # Get the current time again to calculate the RTT
        recvTime = time.time()

        try:
            # Extract the sequence number and server send time from the response message
            ping, seqNum, serverSendTime = response.decode().split()

            # Calculate the round trip time (RTT) in seconds
            rtt = recvTime - sendTime
            RTT.append(rtt)

            # Print the response message and RTT
            print('Ping message', seqNum, 'received from', serverName)
            print('RTT:', rtt, 'seconds\n')
        except ValueError:
            # If the response message is not in the expected format, print the raw message
            print('Received message:', response.decode(), '\n')

    except timeout:
        # If the response times out, print a message
        print('Request timed out\n')
        lost_packets += 1

statistics(RTT, lost_packets)
    
# Close the socket
clientSocket.close()
