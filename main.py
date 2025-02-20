import streamlit as st
from assistant import get_assistance
from config import bot_instructions, greeting
from streamlit_helper import setSidebar, setbg

# Streamlit web app configuration
st.set_page_config(page_title="Burger Queen", page_icon="🍔")
# setbg()

st.title("🍔 Burger Queen")
st.caption("🚀 A chatbot powered by OpenAI")
# st.subheader("Your Virtual Burger Ordering Assistant")

setSidebar()

# A data structure for maintaining the chat history
if "messages" not in st.session_state:
    # Set initial context with role as "system" which sets up the behavior and knowledge for the bot.
    initial_context = {"role": "system", "content": bot_instructions}
    st.session_state.messages = [initial_context]

# Method for adding messages in chat history
def addMessageinChatHistory(msg):     
        st.session_state.messages.append({"role": "user", "content": msg})

# Method for displayinng the chat history
def displayChatHistory():
    first_iteration = True
    for message in st.session_state.messages:
        role, content = message["role"], message["content"]
        if first_iteration:
             content = greeting
             first_iteration = False

        print(f"role:{role}, content:{content}")
        if role == "user":
            st.markdown(f"**You:** {content}")
        else:
            st.markdown(f"**BurgerBot:** {content}")


displayChatHistory()


# Take user Input
# user_input = st.text_input("Type your message:", key="user_input")
user_input = st.chat_input("Type your message:")

# To be invoked when user sends message
# if st.button("Send"):
if user_input:
    addMessageinChatHistory(user_input)

    # Sending all message to OPENAI because OpenAI's ChatCompletion API is contextual. 
    # It generates replies based on the entire conversation history"""
    with st.spinner("BurgerBot is cooking up a reply... 🍔"):
        bot_reply = get_assistance(st.session_state.messages)
    
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    # Updates the chat history by displaying the latest bot response.
    st.rerun()    


