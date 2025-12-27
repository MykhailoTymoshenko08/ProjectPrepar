import os
import requests
import time
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
    
    print(f"🔄 Запит до: {model_name}")
    try:
        response = requests.post(URL, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            choices = result.get('choices', [])
            if choices:
                message = choices[0].get('message', {})
                answer = message.get('content', 'No content')
                return f"✅{answer}"
            return "❌No answer in response"
            
        else:
            try:
                error_data = response.json()
                error_msg = error_data.get('error', {}).get('message', response.text[:200])
            except:
                error_msg = response.text[:200]
            
            return f"❌Error {response.status_code}: {error_msg}"
            
    except requests.exceptions.Timeout:
        return "❌Timeout: server is not responding"
    except requests.exceptions.RequestException as e:
        return f"❌Network error: {str(e)}"
    except Exception as e:
        return f"❌Unexpected error: {str(e)}"
    
def main():
    models = [
        "meta-llama/llama-3.2-3b-instruct",   
        "meta-llama/llama-3.1-8b-instruct",      
        "google/gemini-2.0-flash-exp:free"        
    ]

    prompt = "Explain what an API is in 2 simple sentences."
    
    print(f"Prompt: '{prompt}'")
    print("=" * 60)
    
    successful_models = 0
    
    for i, model in enumerate(models):
        print(f"\n[{i+1}/{len(models)}] Model: {model}")
        
        start_time = time.time()
        answer = get_ai_answer(model, prompt)
        elapsed = time.time() - start_time
        
        print(f"Answer: {answer}")
        print(f"Time: {elapsed:.2f}s")
        print("-" * 60)
        
        if "✅" in answer:
            successful_models += 1
        
        if i < len(models) - 1:
            time.sleep(3)
    
    print(f"\nSummary: {successful_models}/{len(models)} models responded successfully")

if __name__ == "__main__":
    main()