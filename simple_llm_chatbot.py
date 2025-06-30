# simple_llm_chatbot.py

import requests
import os

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
API_TOKEN = os.getenv("HF_API_TOKEN")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}
    except ValueError:
        return {"error": "Invalid JSON response from API"}

def chat():
    print("Simple LLM Chatbot (type 'exit' to quit)")
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            break
        data = query({"inputs": prompt})
        # The response format may vary by model; adjust as needed
        if isinstance(data, dict) and "error" in data:
            print("Bot: (Error)", data["error"])
        else:
            print("Bot:", data[0]["generated_text"].strip())

if __name__ == "__main__":
    chat()