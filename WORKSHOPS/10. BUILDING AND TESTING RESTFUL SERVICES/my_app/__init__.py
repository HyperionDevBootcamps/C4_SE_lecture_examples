from flask import Flask
from .app import main_app
import os

def create_app():
    app = Flask(__name__)  
    
    app.register_blueprint(main_app)
    return app