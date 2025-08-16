from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver, InMemorySaver
from dotenv import load_dotenv


load_dotenv()


llm = ChatOpenAI()

# response = llm.invoke("Which model of GPT are you intrinsically using?").content
# print(response)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)


chatbot = graph.compile(checkpointer=checkpointer)



# Testing for Streming - worked - so implementing it in the frontend

# for message_chunk, metadata in chatbot.stream(
#     {'messages': [HumanMessage(content = 'What is Generative AI. Explain in detail.')]},
#      config = {'configurable': {'thread_id': 'thread_1'}},
#      stream_mode="messages"
# ):
#     if message_chunk.content:
#         print(message_chunk.content, end=" ", flush=True)