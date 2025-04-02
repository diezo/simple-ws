from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handle_message(message):
    print("Received:", message)
    socketio.send(message, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=80, debug=True)
