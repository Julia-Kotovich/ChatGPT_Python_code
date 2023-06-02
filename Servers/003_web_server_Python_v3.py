from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Define the response
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")

# Create an HTTP server with the custom request handler
server_address = ('', 8000)  # Replace with the desired server port number
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Start the server
print("Web server listening on port 8000...")
httpd.serve_forever()
