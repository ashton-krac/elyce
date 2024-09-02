import os

class Config(object):
    """Base config variables."""
    MONGO_URI = os.environ.get('MONGO_URI')  # Get the URI from an environment variable
