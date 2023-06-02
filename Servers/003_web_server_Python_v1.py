from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its corresponding function
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the server
if __name__ == '__main__':
    app.run()
