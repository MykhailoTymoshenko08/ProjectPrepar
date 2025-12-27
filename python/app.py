import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

def ask_ai():
    url = 'https://openrouter.ai/api/v1/chat/completions'
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "meta-llama/llama-3.2-3b-instruct", 
        "messages": [
            {
                "role": "user", 
                "content": "Hi, if you are there write: 'System ready to work'"
            }
        ]
    }   
    
    print("Sending request")
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        answer = result['choices'][0]['message']['content']
        print("Answer from AI: ")
        print(answer)
    else:
        print(f"Error, Code {response.status_code}")
        print(f"Info: {response.text}")

ask_ai()