# UDP Phase #1 Server Process
# By Andrew Woods

from socket import*     # Necessary import for socket programming

serverPort = 12000 # Set port number

serverSocket = socket(AF_INET, SOCK_DGRAM)     # Create UDP socket

serverSocket.bind(("localhost", serverPort))  # Bind socket to 12000 port number

print("The server is ready to receive")

run = True  # Sets run to true to wait for messages

# Loop while run is true
while run:
    message, clientAddress = serverSocket.recvfrom(2048)  # Read from UDP socket into message

    modifiedMessage = message.decode().upper()  # Convert message into upper case form

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)  # Send upper case string back to client

    if message.decode() == 'stop':
        print("Server side has ended!")
        run = False