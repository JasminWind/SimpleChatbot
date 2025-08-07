# filepath: c:\Users\jasmi\OneDrive\Desktop\Python practice\streamlit_chatbot.py
import streamlit as st
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/openai/gpt-oss-120b"
headers = {"Authorization": f"Bearer YOUR_TOKEN_HERE"}

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
    data = query({"prompt": user_input})
    st.write("Bot:", data[0]["generated_text"].strip())