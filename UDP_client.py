# UDP Phase #1 Client Process
# By Andrew Woods

from socket import*     # Include Python's socket library

serverName = "localhost"    # localhost used for running client and server on same machine

serverPort = 12000  # Port number

clientSocket = socket(AF_INET, SOCK_DGRAM)  # Creates UDP socket for server

message = input('Input lowercase sentence:')    # Prompt user for input string

clientSocket.sendto(message.encode(), (serverName, serverPort))     # Attach server name and port to message then send into socket

modifiedMessage, server_address = clientSocket.recvfrom(2048)     # Reply characters from socket converted to string

print(modifiedMessage.decode())     # Prints modified message recieved from the server

clientSocket.close()    # Close the client socket
