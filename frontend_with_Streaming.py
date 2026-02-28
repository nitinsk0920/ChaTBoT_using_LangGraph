import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage
import random
# st.session_state -> dict -> 
chatbot_titles = [
    "What’s on your mind today?",
    "How can I help you right now?",
    "Let’s build something together",
    "Ask me anything",
    "Ready when you are",
    "What would you like to explore?",
    "Got a question?",
    "Start a conversation",
    "Need answers? I’m here.",
    "Type your thoughts..."
]

n= random.randint(0,10)
CONFIG = {'configurable': {'thread_id': 'thread-1'}}
st.title(f"CHAT-BOT ,{chatbot_titles[n]}")
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    
       # first add the message to message_history
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= {'configurable': {'thread_id': 'thread-1'}},
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})