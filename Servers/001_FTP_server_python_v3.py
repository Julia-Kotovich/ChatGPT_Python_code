import socket
import os

# Define FTP server settings
HOST = 'localhost'  # Replace with your FTP server hostname or IP address
PORT = 2121  # Replace with the FTP server port number
USERNAME = 'your_username'  # Replace with your FTP server username
PASSWORD = 'your_password'  # Replace with your FTP server password

# Define FTP server commands
USER_COMMAND = 'USER'
PASS_COMMAND = 'PASS'
LIST_COMMAND = 'LIST'
RETR_COMMAND = 'RETR'
STOR_COMMAND = 'STOR'
QUIT_COMMAND = 'QUIT'

# Define function to handle client connections
def handle_client(client_socket):
    client_socket.send(b'220 Welcome to My FTP Server\r\n')

    authenticated = False

    while True:
        request = client_socket.recv(1024).decode().strip()

        if not request:
            break

        if not authenticated:
            if request.startswith(USER_COMMAND):
                client_socket.send(b'331 User name okay, need password\r\n')
            elif request.startswith(PASS_COMMAND):
                client_socket.send(b'230 User logged in, proceed\r\n')
                authenticated = True
            else:
                client_socket.send(b'530 Not logged in\r\n')
        else:
            if request.startswith(LIST_COMMAND):
                client_socket.send(b'150 Here comes the directory listing\r\n')
                # Perform directory listing logic here
                client_socket.send(b'226 Directory send OK\r\n')
            elif request.startswith(RETR_COMMAND):
                client_socket.send(b'150 Opening data connection\r\n')
                # Perform file download logic here
                client_socket.send(b'226 Transfer complete\r\n')
            elif request.startswith(STOR_COMMAND):
                client_socket.send(b'150 Opening data connection\r\n')
                # Perform file upload logic here
                client_socket.send(b'226 Transfer complete\r\n')
            elif request.startswith(QUIT_COMMAND):
                client_socket.send(b'221 Goodbye\r\n')
                break
            else:
                client_socket.send(b'500 Syntax error, command unrecognized\r\n')

    client_socket.close()

# Create socket and start the FTP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"FTP server listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"New client connected: {client_address[0]}:{client_address[1]}")
    handle_client(client_socket)
