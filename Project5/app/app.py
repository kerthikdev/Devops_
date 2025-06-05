from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)  # Connect to Redis container by name

@app.route('/')
def home():
    count = r.incr('hits')  # Increment "hits" key in Redis
    return f"Hello! This page has been visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Run Flask on container port 5001
