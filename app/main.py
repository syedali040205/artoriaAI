# main.py
import requests

GROQ_API_KEY = "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"
MODEL_NAME = "meta-llama/llama-4-maverick-17b-128e-instruct"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def get_artoria_response(chat_history):
    """Takes chat history, returns Artoria's response"""
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL_NAME,
            "messages": chat_history,
            "temperature": 0.7,
            "max_tokens": 400
        }
    )
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    raise Exception(f"API Error: {response.status_code} - {response.text}")

# Only run the CLI interface if executed directly
if __name__ == "__main__":
    chat_history = [
        {"role": "system", "content": (
            "You are Artoria Pendragon, also known as Saber...you were summoned in present era and have all the knowledge and things about this era"
        )}
    ]
    
    print("🗡️ Artoria Pendragon Chatbot (type 'exit' to leave)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Farewell, Master. May the light guide your path.")
            break

        chat_history.append({"role": "user", "content": user_input})
        reply = get_artoria_response(chat_history)
        print("Artoria:", reply)
        chat_history.append({"role": "assistant", "content": reply})