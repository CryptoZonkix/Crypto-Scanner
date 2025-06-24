import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecret')
    CORS(app)
    db.init_app(app)
    socketio.init_app(app)
    from app.api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")
    return app
