# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from main import get_artoria_response  # Import your existing function

app = Flask(__name__)
CORS(app)

SYSTEM_PROMPT = {
    "role": "system", 
    "content": "You are Artoria Pendragon..."  # Same as in main.py
}

# Simple in-memory storage (replace with database in production)
conversations = {}

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get('user_id', 'default')
    message = data['message']
    
    # Initialize conversation if new user
    if user_id not in conversations:
        conversations[user_id] = [SYSTEM_PROMPT]
    
    # Add user message
    conversations[user_id].append({"role": "user", "content": message})
    
    # Get response using your existing function
    try:
        reply = get_artoria_response(conversations[user_id])
        conversations[user_id].append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear():
    return jsonify({"status": "conversation cleared"})

if __name__ == '__main__':
    app.run(port=5000)