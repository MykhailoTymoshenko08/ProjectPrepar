import os
import requests
import time
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_ai():
    user_message = request.json.get('message')
    model = request.json.get('model', 'meta-llama/llama-3.2-3b-instruct')
    
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": model,
        "messages": [{"role": "user", "content": user_message}]
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        answer = response.json()['choices'][0]['message']['content']
        return jsonify({"success": True, "answer": answer})
    else:
        return jsonify({"success": False, "error": f"Помилка {response.status_code}"})

if __name__ == '__main__':
    app.run(debug=True)