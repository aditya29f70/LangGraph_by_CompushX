import os
from langgraph.graph import StateGraph, START, END, add_messages
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate



llm= HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2" ,
    task="chat-completions",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=25
)

model= ChatHuggingFace(llm=llm)



class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage], add_messages]



def chat_interaction(state:ChatState):

    messages= [SystemMessage(content="You are a Question Answering Chat bot, and if you don't know anythings just tell you don't know instead of telling irrelevent things"),*state['messages']]

    prompt= ChatPromptTemplate.from_messages(messages)

    parser= StrOutputParser()

    chain= prompt|model|parser

    result= chain.invoke({})

    return {"messages":[AIMessage(content=result)]}






builder= StateGraph(ChatState)

builder.add_node("chat_response", chat_interaction)

builder.add_edge(START, "chat_response")
builder.add_edge("chat_response", END)

checkpointer= InMemorySaver()

graph= builder.compile(checkpointer=checkpointer)

print(graph)

config1= {"configurable":{"thread_id":1}}


# while True:
#     user_input= input("User: ")
#     print(f"User: {user_input}")

#     if user_input.strip().lower() in ['stop', 'end']:
#         break
#     else:
#         graph_resp= graph.invoke({"messages":[HumanMessage(content=user_input)]}, config=config1)['messages'][-1].content

#         print(f"AI: {graph_resp}")





