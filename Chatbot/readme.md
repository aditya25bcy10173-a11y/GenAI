📚 Mood‑Based Mistral Chatbot – README

A lightweight Python chatbot that lets you switch between Angry, Funny, and Sad personalities on the fly.
Uses Mistral‑small‑2506 via langchain_mistralai and offers both a console UI (chatbot.py) and a Streamlit web UI (Ulchatbot.py).

🎯 Overview
What	Why
Multi‑mood AI	Pick a tone (Angry / Funny / Sad) and the model responds accordingly.
Two interfaces	Fast console interaction for debugging & a modern Streamlit UI for a richer experience.
Zero‑code setup	Just install a few Python packages, drop an API key in .env, and you’re ready to chat.
🗂️ Project Structure
D:\gen AI\chatbot
│   .env                ← API key (MISTRAL_API_KEY)
│   README.md           ← **You are here**
│   requirements.txt    ← Python dependencies
│   chatbot.py          ← Console version
│   Ulchatbot.py        ← Streamlit web version
│   huggingface.py      ← (placeholder)
│   locolmodal.py
│   test.py
│
└─myenv/                ← optional virtual‑env (created by you)
📦 Requirements
Category	Packages	Install command
Core	python-dotenv
langchain
langchain_mistralai
streamlit	pip install -r requirements.txt
Optional	uvicorn (if you want to expose via ASGI)	pip install uvicorn

Tip: All versions are compatible with Python ≥ 3.9.

⚙️ Configuration

Create a file named .env in the project root with your Mistral API key:

text
MISTRAL_API_KEY="sk‑YOUR_MISTRAL_KEY_HERE"

Do not surround the key with extra spaces or quotes other than the double quotes shown.

🚀 Installation & First Run

The commands below assume you are in a PowerShell or CMD terminal.
If you prefer a virtual environment (recommended), follow the optional steps first.

1️⃣ (Optional) Create & activate a virtual environment
powershell
# Create the env
python -m venv myenv   # or: py -m venv myenv
# Activate it
# PowerShell
.\myenv\Scripts\Activate.ps1
# CMD
myenv\Scripts\activate.bat
# Git‑Bash / WSL
source myenv/Scripts/activate
2️⃣ Install dependencies
powershell
pip install -r requirements.txt
3️⃣ Run the console version
powershell
python chatbot.py

You’ll see a prompt like:

chosse your AI mode
press 1 for Angry mode
press 2 for funny mode 
press 3 for sad mode
tell your response :- 1

Pick 1, 2, or 3. Type 0 anytime to exit.

4️⃣ Run the Streamlit web UI
powershell
streamlit run Ulchatbot.py

A browser tab opens at http://localhost:8501 (or copy the URL from the terminal).
Use the radio‑button at the top to switch moods, then type messages in the chat input.

📈 Architecture & Data Flow
.env → loads MISTRAL_API_KEY.
ChatMistralAI receives the key and serves each request.
Mood selection determines the system prompt (SystemMessage).
All user & AI messages are stored in a session list (messages).
🛠️ Usage Details
Feature	Console (chatbot.py)	Streamlit UI (Ulchatbot.py)
Mood switch	Choose 1/2/3 at start.	Radio button at the top (🔴 Angry, 😂 Funny, 😢 Sad).
End session	Type 0.	Click the 🔄 Reset Chat button or type 0.
Message history	Printed at the end (print(messages)).	Persisted in Streamlit st.session_state.
Error handling	Raises RuntimeError if the key is missing.	Same check; Streamlit shows a warning banner.
📜 License

MIT License – feel free to fork, modify, and use in your own projects.

🙋‍♀️ Getting Help
Missing Python? Install from https://www.python.org/downloads/
 and ensure the installer adds Python to your PATH.
Dependency errors? Run pip install --upgrade pip setuptools wheel then retry pip install -r requirements.txt.
API‑key problems? Double‑check the value in .env – it must be exactly the string you copied from the Mistral console, wrapped in double quotes.
🎉 You're all set!

Run the commands, pick a mood, and start chatting with your new AI buddy. Enjoy!
