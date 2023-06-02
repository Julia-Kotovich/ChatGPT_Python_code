from ftplib import FTP

# Define FTP server settings
HOST = 'localhost'  # Replace with your FTP server hostname or IP address
PORT = 21  # Replace with the FTP server port number
USERNAME = 'your_username'  # Replace with your FTP server username
PASSWORD = 'your_password'  # Replace with your FTP server password

# Define function to handle client connections
def handle_client(client):
    client.send(b'220 Welcome to My FTP Server\n')

    while True:
        request = client.recv(1024).decode()
        if not request:
            break

        if request.startswith('USER'):
            client.send(b'331 User name okay, need password\n')
        elif request.startswith('PASS'):
            client.send(b'230 User logged in, proceed\n')
        elif request.startswith('LIST'):
            client.send(b'150 Here comes the directory listing\n')
            # Perform directory listing logic here
            client.send(b'226 Directory send OK\n')
        elif request.startswith('RETR'):
            client.send(b'150 Opening data connection\n')
            # Perform file download logic here
            client.send(b'226 Transfer complete\n')
        elif request.startswith('STOR'):
            client.send(b'150 Opening data connection\n')
            # Perform file upload logic here
            client.send(b'226 Transfer complete\n')
        elif request.startswith('QUIT'):
            client.send(b'221 Goodbye\n')
            break
        else:
            client.send(b'500 Syntax error, command unrecognized\n')

    client.close()

# Create FTP server instance
ftp_server = FTP()
ftp_server.bind((HOST, PORT))

# Set FTP server credentials
ftp_server.login(USERNAME, PASSWORD)

# Start listening for client connections
ftp_server.listen(5)
print(f"FTP server listening on {HOST}:{PORT}")

while True:
    client, addr = ftp_server.accept()
    print(f"New client connected: {addr[0]}:{addr[1]}")
    handle_client(client)
