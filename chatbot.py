import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

def get_model():
    mistral_key = os.getenv("MISTRAL_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    # If MISTRAL_API_KEY starts with 'sk-', it's actually an OpenAI key
    if mistral_key and mistral_key.startswith("sk-"):
        openai_key = mistral_key
        mistral_key = None
        
    if mistral_key:
        from langchain_mistralai import ChatMistralAI
        return ChatMistralAI(model="mistral-small-2506", temperature=0.9, api_key=mistral_key)
    elif openai_key:
        try:
            from langchain_openai import ChatOpenAI
            return ChatOpenAI(model="gpt-4o-mini", temperature=0.9, api_key=openai_key)
        except ImportError:
            raise RuntimeError(
                "\n[!] You are using an OpenAI key (sk-proj-...), but 'langchain-openai' is not installed.\n"
                "    Run this command in your terminal:\n"
                "        pip install langchain-openai\n"
                "    Or if you want Mistral, get a key from https://console.mistral.ai/ and set MISTRAL_API_KEY in .env"
            )
    else:
        raise RuntimeError("No API key found! Please set MISTRAL_API_KEY or OPENAI_API_KEY in .env")

model = get_model()

print("Choose your AI mode:")
print("press 1 for Angry mode")
print("press 2 for Funny mode")
print("press 3 for Sad mode")

try:
    choice = int(input("Tell your response (1/2/3):- "))
except ValueError:
    choice = 2

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."
else:
    mode = "You are a very funny AI agent. You respond with humor and jokes."

messages = [
    SystemMessage(content=mode)
]

print("----------------- Welcome! Type 0 to exit -----------------")
while True:
    prompt = input("You : ")
    if prompt.strip() == "0":
        print("Bot : Goodbye!")
        break
    if not prompt.strip():
        continue
        
    messages.append(HumanMessage(content=prompt))
    try:
        response = model.invoke(messages)
        messages.append(AIMessage(content=response.content))
        print("Bot :", response.content)
    except Exception as e:
        print(f"\n[Error from AI Provider]: {e}")
        break
