# filepath: c:\Users\jasmi\OneDrive\Desktop\Python practice\streamlit_chatbot.py
import streamlit as st
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
API_TOKEN = os.getenv("HF_API_TOKEN")
print("API_TOKEN:", API_TOKEN)  # <-- Add this line for debugging
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return [{"generated_text": f"(Error) {e}"}]

st.title("Simple LLM Chatbot")
user_input = st.text_input("You:", "")
if user_input:
    data = query({"inputs": user_input})
    st.write("Bot:", data[0]["generated_text"].strip())