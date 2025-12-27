import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
URL = 'https://openrouter.ai/api/v1/chat/completions'

def get_ai_answer(model_name, user_text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model_name, 
        "messages": [
            {
                "role": "user", 
                "content": user_text
            }
        ],
        "max_tokens": 150
    }   
    
    print(f"Request to {model_name}")
    try:
        response = requests.post(URL, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            answer = result['choices'][0]['message']['content']
            return f"✅{answer}"
        else:
            error = response.json().get('error', {}).get('message', 'Unknown error')
            return f"❌Error {response.status_code}: {error}"
            
    except requests.exceptions.Timeout:
        return "❌Timeout. Server is not responding"
    except Exception as e:
        return f"❌Request error: {str(e)}"
    

print("Write your request")
prompt = input()

def main(promptM):
    models = [
        "meta-llama/llama-3.2-3b-instruct",   
        "meta-llama/llama-3.1-8b-instruct",      
        #"google/gemini-2.0-flash-exp:free"        
    ]

    
    print(f"Sending request '{promptM}'")
    print("=" * 60)
    
    for i, model in enumerate(models):
        print(f"\n[{i+1}/{len(models)}] Model: {model}")
        answer = get_ai_answer(model, promptM)
        print(f"Answer:\n\n\t {answer}")
        print("-" * 60)

    print("Write your request")
    prompt = input()
    if prompt == 0:
        exit()
    else:
        main(prompt)    


if __name__ == "__main__":
    main(prompt)