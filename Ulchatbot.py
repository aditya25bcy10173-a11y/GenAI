import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Mood Based AI Chatbot")
st.caption("Choose AI personality and start chatting | Type 0 to stop")

# ---------------- MODEL INITIALIZATION ----------------
@st.cache_resource
def get_model():
    mistral_key = os.getenv("MISTRAL_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    # If key starts with 'sk-', it is an OpenAI key
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
            st.error(
                "You have an OpenAI key in your `.env`, but `langchain-openai` is not installed! "
                "Run `pip install langchain-openai` in your terminal."
            )
            st.stop()
    else:
        st.error("No API key found in `.env`! Please add `MISTRAL_API_KEY` or `OPENAI_API_KEY`.")
        st.stop()

model = get_model()

# ---------------- MODE SELECTION ----------------
mode_choice = st.radio(
    "Choose your AI Mode:",
    ["😡 Angry", "😂 Funny", "😢 Sad"],
    horizontal=True
)

if mode_choice == "😡 Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_choice == "😂 Funny":
    mode = "You are a very funny AI agent. You respond with humor and jokes."
else:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# ---------------- SESSION MEMORY ----------------
if "messages" not in st.session_state or st.session_state.get("current_mode") != mode:
    st.session_state.current_mode = mode
    st.session_state.messages = [SystemMessage(content=mode)]

# ---------------- DISPLAY CHAT HISTORY ----------------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Say something...")

if user_input:
    if user_input.strip() == "0":
        st.warning("Conversation ended. Click 'Reset Chat' below to start fresh.")
        st.stop()

    # Add and render user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response with error handling
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.invoke(st.session_state.messages)
                st.session_state.messages.append(AIMessage(content=response.content))
                st.write(response.content)
            except Exception as e:
                st.error(f"Error calling model: {e}")

# ---------------- CLEAR BUTTON ----------------
st.divider()
if st.button("🔄 Reset Chat"):
    st.session_state.messages = [SystemMessage(content=mode)]
    st.rerun()
