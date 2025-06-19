from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Kerthik ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
