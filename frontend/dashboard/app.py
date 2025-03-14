from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import requests

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

BACKEND_URL = "http://localhost:5000"

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    print("Client connected")

# API to execute trade
@app.route("/trade", methods=["POST"])
def execute_trade():
    data = request.json
    response = requests.post(f"{BACKEND_URL}/trade", json=data)
    return jsonify(response.json())

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)
