import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    MONGO_URI = os.environ.get('MONGO_URI')  # Get the URI from an environment variable

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    MONGO_URI = os.environ.get('MONGO_URI')  # Get the URI from an environment variable
