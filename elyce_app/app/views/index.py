from flask import Blueprint

mod_index = Blueprint('index', __name__)

@mod_index.route('/')
def hello_world():
    return 'Hello, World!'

# from flask import Blueprint, jsonify
# from app.extensions import mongo

# mod_index = Blueprint('index', __name__)

# @mod_index.route('/')
# def home():
#     user = mongo.db.test.find_one()
#     if user:
#         return jsonify(user), 200
#     else:
#         return jsonify(message="No user found"), 404

# @mod_index.route('/add')
# def add_data():
#     mongo.db.test.insert_one({'name': 'Test User'})
#     return jsonify(message="Data added"), 200

# @mod_index.route('/fetch')
# def fetch_data():
#     user = mongo.db.test.find_one({'name': 'Test User'})
#     return jsonify(user=user), 200