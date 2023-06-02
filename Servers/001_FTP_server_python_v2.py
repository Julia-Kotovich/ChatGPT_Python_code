from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define FTP server settings
HOST = 'localhost'  # Replace with your FTP server hostname or IP address
PORT = 2121  # Replace with the FTP server port number
USERNAME = 'your_username'  # Replace with your FTP server username
PASSWORD = 'your_password'  # Replace with your FTP server password

# Create a dummy authorizer for managing user authentication
authorizer = DummyAuthorizer()
authorizer.add_user(USERNAME, PASSWORD, '/path/to/home', perm='elradfmw')

# Define a custom FTP handler class
class MyFTPHandler(FTPHandler):
    pass

# Set the authorizer for the FTP handler
MyFTPHandler.authorizer = authorizer

# Create the FTP server instance
ftp_server = FTPServer((HOST, PORT), MyFTPHandler)

# Start the FTP server
print(f"FTP server listening on {HOST}:{PORT}")
ftp_server.serve_forever()
