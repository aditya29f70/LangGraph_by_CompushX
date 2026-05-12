import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END, add_messages
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3


load_dotenv()


llm= HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
    task='chat-completions',
    temperature=0.7,
    repetition_penalty=1.2,
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


# creating a database for checkpoint
conn= sqlite3.connect(database='./chatbot.db', check_same_thread=False) # so it will great that name database if there is not any database is created with that name 

# for checkpointer
checkpointer= SqliteSaver(conn=conn)



builder= StateGraph(ChatState)

builder.add_node('chat_handle', chat_handle)

builder.add_edge(START, 'chat_handle')
builder.add_edge("chat_handle", END)



graph= builder.compile(checkpointer=checkpointer)


config1= {'configurable':{'thread_id':1}}


# stream= graph.stream({'messages':[HumanMessage(content='hi')]}, stream_mode='messages', config=config1)
#     # diff kinds of stream_mode we have like messages, values, custom etc ; we will use rest of stream mode when work with agentic ai workflow

# # stream is a generator 

# print(f"Type of stream; {type(stream)}")

# # now with help of this generator we have to process output token by token ;; by using loop 

# for message_chunk, metadata in stream:
#     if message_chunk.content:
#         print(message_chunk.content,end=' ', flush=True)


# now have to write query which give ideal about how many threads we have in our database
# so we have checkpointer (SqliteSaver) so it has function called ''list'' which has power to give all the thread id or all checkpointer id in a thread
# eg. checkpointer.list(None) -> means we want all checkpointers not for a particular thread

def retrieve_all_thread_ids(checkpointer):
    all_threads= set()
    for checkpointer in checkpointer.list(None):
        all_threads.add(checkpointer.config['configurable']['thread_id'])

    return list(all_threads)