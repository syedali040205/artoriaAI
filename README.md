# Artoria AI - Saber Chatbot

Artoria Pendragon (Saber) AI Assistant

A conversational AI interface featuring Artoria Pendragon (Saber) from the Fate franchise, with animated expressions and character-appropriate responses.

## Features
- 🗡️ Character-authentic responses as Artoria Pendragon
- 🎭 4 dynamic expressions (idle/thinking/explaining/sad)
- ⚔️ Fate/stay night themed UI with Excalibur elements
- 💬 Interactive chat with typing animations
- 🌓 Light/dark mode toggle

## Installation
1. Clone repo:
```bash
git clone https://github.com/yourusername/artoria-ai.git
cd artoria-ai
Install dependencies:

bash
pip install -r requirements.txt
Add Groq API key to main.py:

python
GROQ_API_KEY = "your_api_key_here"
Usage
Start backend:

bash
python app.py
Open frontend:

bash
python -m http.server 5000
Then visit http://localhost:5000

Files
artoria-ai/
├── assets/expressions/  # Character images
├── app.py              # Flask backend
├── main.py             # Groq API handler
├── index.html          # Web interface
├── requirements.txt    # Dependencies
└── README.md
Configuration (in main.py)
MODEL_NAME: meta-LLaMa4-maverick

SYSTEM_PROMPT: Adjust personality

TEMPERATURE: Set creativity (0.7 recommended)

Requirements
Python 3.8+

Groq API key

Modern browser

License
MIT License

"Saber" and "Fate" are TM of TYPE-MOON. This is a fan project not affiliated with TYPE-MOON.


Key points included:
1. Clear project description
2. Installation/usage instructions
3. File structure overview
4. Configuration options
5. Legal disclaimer
6. Emoji visual hierarchy
7. Copy-paste ready code blocks
