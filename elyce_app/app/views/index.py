from flask import render_template, Blueprint

# mod_index = Blueprint('index', __name__)

# @mod_index.route('/')
# def hello_world():
#     return 'Hello, World!'


# You might already have a blueprint setup for this in app/views/__init__.py
index_bp = Blueprint('index', __name__, template_folder='templates')

@index_bp.route('/')
def home():
    return render_template('index.html')

# Ensure this blueprint is registered in your app/__init__.py