import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Initialize model
model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

# Mode selection
mode_option = st.selectbox(
    "Choose your AI mode",
    ["Angry", "Funny", "Sad", "AI"]
)

# Mode logic (same as your CLI code)
if mode_option == "Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_option == "Funny":
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif mode_option == "Sad":
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."
else:
    mode = "You are a helpful and intelligent AI assistant. You respond clearly and helpfully."

# Initialize messages (only once)
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]

# Show chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response
    response = model.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)