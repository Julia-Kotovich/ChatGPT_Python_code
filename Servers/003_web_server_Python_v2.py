import socket

# Define server settings
HOST = 'localhost'  # Replace with your server hostname or IP address
PORT = 8000  # Replace with the desired server port number

# Define HTTP response
response = """HTTP/1.1 200 OK
Content-Type: text/html

<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
"""

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print(f"Web server listening on {HOST}:{PORT}")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"New client connected: {client_address[0]}:{client_address[1]}")

    # Receive the client request
    request = client_socket.recv(1024).decode()
    print(f"Received request:\n{request}")

    # Send the HTTP response
    client_socket.sendall(response.encode())

    # Close the client connection
    client_socket.close()
