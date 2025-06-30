# simple_llm_chatbot.py

from transformers import pipeline

# Load a small pre-trained GPT-2 model
generator = pipeline('text-generation', model='distilgpt2')

def chat():
    print("Simple LLM Chatbot (type 'exit' to quit)")
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            break
        response = generator(prompt, max_length=50, num_return_sequences=1)
        print("Bot:", response[0]['generated_text'][len(prompt):].strip())

if __name__ == "__main__":
    chat()