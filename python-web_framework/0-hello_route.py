from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/', strict_slashes=False) 
def hello_hbnb():
    #Return the desired response
    return 'Hello HBNB!'

# Start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
