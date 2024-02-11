# UDP Phase #1 Server Process
# By Andrew Woods

from socket import*     # Necessary import for socket programming
from PIL import Image   # Pillow Library used for importing image
import numpy as np      # Numpy Library used for image -> array conversion

# Initialize server socket communication
serverPort = 12000  # Set port number
serverSocket = socket(AF_INET, SOCK_DGRAM)     # Create UDP socket
serverSocket.bind(("localhost", serverPort))  # Bind socket to 12000 port number

print("The server is ready to receive")

packets_recv = 0    # Tracks number of packets received from client
recv_image = np.zeros(256 * 256, dtype=np.uint8)    # Initialize image array for received packets
packet_num = 0

# Loop while run is true
while packets_recv < 64:
    Packet, clientAddress = serverSocket.recvfrom(2048)  # Read from UDP socket into message
    packet = np.frombuffer(Packet, dtype=np.uint8)       # convert packet back into an array of 8-bit integers

    pixels = np.zeros_like(packet)      # Creates a new array that identical to packet and is accessible
    pixels[0:] = packet[0:]             # Copies all data from packet into pixels array

    pixels[0] = packet_num              # Assigns first value from packet as the packet num
    image_index = packet_num * 1024

    # Loop through packet, assigning each pixel in the packet to the reconstructed image array
    for i in range(1024):
        recv_image[image_index] = pixels[i + 1]
        image_index += 1

    packets_recv += 1   # Increment number of packets received and the current packet number
    packet_num += 1

print(f"{packets_recv} Packets Received")   # Packet Print statement

# Modify 1D array into a 2D array
recv_image_2D = recv_image.reshape((256, 256))

# Convert array to BMP file
output_image = Image.fromarray(recv_image_2D)

# Display Image
output_image.save('Received_Chelsea_Logo.bmp')
output_image.show()
