import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)
print(f"Connected to {server_address}")

# Send a message to the server
message = "Hello from the client!"
client_socket.send(message.encode('utf-8'))

# Receive the response from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode('utf-8')}")

# Close the socket
client_socket.close()
