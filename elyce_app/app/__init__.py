from flask import Flask
from .views.index import mod_index  # Import the blueprint

def create_app():
    app = Flask(__name__)

    # Register the blueprint from the views module
    app.register_blueprint(mod_index)

    return app

# from flask import Flask
# from .extensions import mongo
# from .config import Config
# from .views.index import mod_index
# import os
# from dotenv import load_dotenv
# load_dotenv()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)  # Make sure Config class properly imports the MONGO_URI
#     app.config['MONGO_URI'] = os.getenv('MONGO_URI')  # Additionally set MONGO_URI from the environment variable

#     if not app.config['MONGO_URI']:
#         raise RuntimeError("MONGO_URI not set in environment variables")

#     mongo.init_app(app)
#     app.register_blueprint(mod_index)
#     return app
