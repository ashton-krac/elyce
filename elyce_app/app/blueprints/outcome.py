from flask import request, jsonify, current_app, Blueprint
from pymongo import MongoClient
import openai

outcome_bp = Blueprint('outcome', __name__)

# MongoDB setup
client = MongoClient(current_app.config['MONGO_URI'])
db = client.your_database_name
bets_collection = db.bets

@outcome_bp.route('/process', methods=['POST'])
def process_input():
    user_input = request.form['user_input']
    
    # OpenAI API call
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate the following goal into a specific and quantifiable outcome:\n\n'{user_input}'",
        max_tokens=150
    )
    
    outcome = response.choices[0].text.strip()
    
    # Save to MongoDB
    bet = {
        'user_input': user_input,
        'outcome': outcome
    }
    bets_collection.insert_one(bet)
    
    return jsonify({'outcome': outcome})

# Make sure to import this blueprint in your app/__init__.py and register it
