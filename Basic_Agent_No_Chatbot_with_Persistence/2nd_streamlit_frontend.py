import streamlit as st
from langgraph_backend import *


# This method still fails to retain the thread because each time the user inputs a message the list is also empty
# Therefore, streamlit comes with a feature called session_state
# message_history = []


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# for message in message_history:
#     with st.chat_message(message['role']):
#         st.text(message['message'])

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['message'])

# Testing
# with st.chat_message('user'):
#     st.text('Hi')

# with st.chat_message('AI'):
#     st.text('How may I help you?')


# user_input = st.chat_input('Type Here')

# if user_input:
#     with st.chat_message('user'):
#         st.text(user_input)

CONFIG = {'configurable': {'thread_id': '1'}}
user_input = st.chat_input('Type here...')

if user_input:

    st.session_state['message_history'].append({'role': 'user', 'message': user_input})
    with st.chat_message('user'):
        st.text(user_input)


    response = chatbot.invoke({'messages': [HumanMessage(content = user_input)]}, config = CONFIG)
    ai_message = response['messages'][-1].content
    st.session_state['message_history'].append({'role': 'AI', 'message': ai_message})

    with st.chat_message('AI'):
        st.text(ai_message)

    # with st.chat_message('AI'):
    #     response = llm.invoke(st.session_state['message_history'][-1]['message']).content
    #     st.session_state['message_history'].append({'role': 'AI', 'message': response})
    #     st.text(response)

