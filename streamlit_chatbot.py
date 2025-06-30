# filepath: c:\Users\jasmi\OneDrive\Desktop\Python practice\streamlit_chatbot.py
import streamlit as st
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
API_TOKEN = os.getenv("HF_API_TOKEN")

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return [{"generated_text": f"(Error) {e}"}]

st.set_page_config(page_title="Simple LLM Chatbot", page_icon="🤖")
st.title("🤖 Simple LLM Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input and send button
user_input = st.text_input("Type your message:", key="input")
send = st.button("Send")

if send and user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Query the model
    data = query({"inputs": user_input})
    bot_reply = data[0]["generated_text"].strip() if isinstance(data, list) and "generated_text" in data[0] else "(Error) No response"
    # Add bot reply to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    # Rerun to display new messages
    st.rerun()