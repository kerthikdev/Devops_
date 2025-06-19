from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask inside Docker , we are using Dockerfile to build this image"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
