from flask import Flask
from .views.index import mod_index  # Import the blueprint

def create_app():
    app = Flask(__name__)

    # Register the blueprint from the views module
    app.register_blueprint(mod_index)

    return app