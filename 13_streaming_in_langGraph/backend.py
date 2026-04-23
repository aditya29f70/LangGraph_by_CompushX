import os
from langgraph.graph import StateGraph, START, END, add_messages
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langgraph.checkpoint.memory import InMemorySaver


llm= HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task='chat-completions',
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm=llm)



class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage], add_messages]



def chat_handle(state:ChatState):
    messages= [SystemMessage(content="You are question answering chat bot, and if you don't know about anything which is asked please tell that you don't know instead of telling irrelavent response"), *state['messages']]

    prompt= ChatPromptTemplate.from_messages(messages)

    parser= StrOutputParser()

    chain= prompt| model|parser 

    result= chain.invoke({})

    return {"messages":[AIMessage(content=result)]}



builder= StateGraph(ChatState)

builder.add_node('chat_handle', chat_handle)

builder.add_edge(START, 'chat_handle')
builder.add_edge("chat_handle", END)


checkpointer= InMemorySaver()

graph= builder.compile(checkpointer=checkpointer)


config1= {'configurable':{'thread_id':1}}





