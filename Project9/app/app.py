# app/app.py
from flask import Flask
import logging

app = Flask(__name__)

# Configure logging to file
logging.basicConfig(filename='/var/log/flask_app.log', level=logging.INFO)

@app.route('/')
def hello():
    app.logger.info('Hello endpoint was reached.')
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
