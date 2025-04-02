import os
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handle_message(message):
    print("Received:", message)
    socketio.send(message, broadcast=True)

if __name__ != "__main__":  # Gunicorn import fix
    gunicorn_app = app  # Gunicorn needs a callable Flask app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    socketio.run(app, host="0.0.0.0", port=port)
