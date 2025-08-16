import streamlit as st
from langgraph_backend_stream import *


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['message'])



CONFIG = {'configurable': {'thread_id': '1'}}
user_input = st.chat_input('Type here...')

if user_input:

    st.session_state['message_history'].append({'role': 'user', 'message': user_input})
    with st.chat_message('user'):
        st.text(user_input)



    

    with st.chat_message('AI'):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {"messages": HumanMessage(content = user_input)},
                config = CONFIG,
                stream_mode="messages"
            )
        )

    st.session_state['message_history'].append({'role': 'AI', 'message': ai_message})


