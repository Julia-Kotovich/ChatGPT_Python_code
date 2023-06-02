import socket
import threading

# Define server settings
HOST = 'localhost'  # Replace with your server hostname or IP address
PORT = 8000  # Replace with the desired server port number

# Define HTTP response
response_template = """HTTP/1.1 {status}
Content-Type: text/html

{content}
"""

# Function to handle client requests
def handle_request(client_socket):
    request = client_socket.recv(1024).decode()

    # Parse the HTTP request
    headers, body = request.split('\r\n\r\n')
    method, path, protocol = headers.split('\r\n')[0].split(' ')

    # Handle GET request
    if method == 'GET':
        if path == '/':
            content = "<h1>Hello, World!</h1>"
            response = response_template.format(status='200 OK', content=content)
        else:
            content = "<h1>404 Not Found</h1>"
            response = response_template.format(status='404 Not Found', content=content)
    
    # Handle POST request
    elif method == 'POST':
        # Add your logic for handling POST requests here
        content = "<h1>POST request received</h1>"
        response = response_template.format(status='200 OK', content=content)

    # Send the HTTP response
    client_socket.sendall(response.encode())

    # Close the client connection
    client_socket.close()

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"HTTP server listening on {HOST}:{PORT}")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"New client connected: {client_address[0]}:{client_address[1]}")

    # Create a new thread to handle the request
    thread = threading.Thread(target=handle_request, args=(client_socket,))
    thread.start()
