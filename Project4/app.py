from flask import Flask
import os
from dotenv import load_dotenv  # Import the dotenv package

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello():
    app_name = os.getenv("APP_NAME", "DefaultApp")
    return f"Welcome to {app_name}!"

if __name__ == '__main__':
    # Get the port from the environment variable
    port = os.getenv("PORT")  # Default to 5000 if PORT is not set
    # print(f"Running on port: {port}")
    app.run(host='0.0.0.0', port=int(port))f