from http.server import HTTPServer, BaseHTTPRequestHandler

# Define the request handler class
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Hello, World!</h1></body></html>')

# Define server settings
HOST = 'localhost'  # Replace with your server hostname or IP address
PORT = 8000  # Replace with the desired server port number

# Create HTTP server instance
http_server = HTTPServer((HOST, PORT), MyHTTPRequestHandler)

# Start the server
print(f"HTTP server listening on {HOST}:{PORT}")
http_server.serve_forever()
