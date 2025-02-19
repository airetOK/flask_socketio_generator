template = """from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import logging

socketio = SocketIO()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socketio.init_app(app)

    @app.route("/")
    def main():
        return render_template("index.html")

    @socketio.on("join")
    def connect(json):
        logger.info(f"Received json: {str(json)}")

    @socketio.on("my event")
    def handle_my_event():
        emit("my event response", "Server says that %s is great!", broadcast=True)

    return app

if __name__ == '__main__':
    app = create_app()
    socketio.run(app)
"""
