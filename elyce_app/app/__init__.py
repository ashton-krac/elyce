from flask import Flask
from .config import Config
from .views.index import index_bp
from .extensions import mongo
# from .views.index import mod_index  # Import the blueprint
from dotenv import load_dotenv
load_dotenv()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # mongo.init_app(app)  # Initialize PyMongo

    from .views.index import index_bp
    app.register_blueprint(index_bp)

    return app



# def create_app():
#     app = Flask(__name__)

#     # Register the blueprint from the views module
#     app.register_blueprint(mod_index)

#     return app