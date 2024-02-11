# UDP Phase #2 Client Process
# By Andrew Woods

from socket import*     # Include Python's socket library
from PIL import Image   # Pillow Library used for importing image
import numpy as np      # Numpy Library used for image -> array conversion


# Initialize socket communication
serverName = "localhost"    # localhost used for running client and server on same machine
serverPort = 12000  # Port number
clientSocket = socket(AF_INET, SOCK_DGRAM)  # Creates UDP socket for server

# Image File Path
image_path = r"C:\Users\awood\Desktop\UDP_Phase2\Chelsea-FC-icon.bmp"    # raw(r) string needed due to \

# Load Image and convert to greyscale
image = Image.open(image_path)
grey_image = image.convert("L")
grey_image.show()

# Convert Image to numpy array of unsigned 8-bit integer
image_array = np.array(grey_image, dtype=np.uint8)

# Use Flatten() to convert to 1D array
image_array_1D = image_array.flatten()

#   print(image_array_1D)

# Initialize Packet Info
packet_size = 1025


# Loop through all packets
# Track: Index of image array, packet number,
for packet_num in range(64):                                                    # Loop through 64 packets
    Packet = np.zeros(1025, dtype=np.uint8)                               # Initialize new packet array of zeros with default type 8-bit unsigned int
    Packet[0] = packet_num                                                      # Set first index of packet to packet_num

    for pixel_num in range(1024):                                               # Loop through 1024 pixels
        Packet[pixel_num + 1] = image_array_1D[packet_num * 1024 + pixel_num]   # Set Packet 1-1025 values to match image

    packet_bytes = Packet.tobytes()                                             # Convert Packet array to bytes
    print(Packet)
    print(packet_bytes)
    clientSocket.sendto(packet_bytes, (serverName, serverPort))    # Encode packet and send to server

clientSocket.close()    # Close the client socket



