import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END, add_messages
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_groq import ChatGroq
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

from langchain_community.tools import DuckDuckGoSearchRun
import requests

from langchain.tools import tool 
from langgraph.prebuilt import ToolNode, tools_condition


os.environ['LANGCHAIN_PROJECT']= "Chat-bot+Observability"

load_dotenv()


# llm= HuggingFaceEndpoint(
#     repo_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
#     task='chat-completions',
#     temperature=0.7,
#     repetition_penalty=1.2,
#     huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# model= ChatHuggingFace(llm=llm)



#******************************** Tools ****************************************************

search_internet= DuckDuckGoSearchRun(region= "us-en")

@tool
def calculater(first_num:float, second_num:float, operation:str)-> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: addition(add), substraction(sub), multiplication(mul), division(div)
    """
    try:
        if operation=='add':
            result= first_num+ second_num

        elif operation=='sub':
            result= first_num-second_num

        elif operation=='mul':
            result= first_num* second_num
        elif operation=='div':
            if second_num==0:
                result= {"error":"division by zero is not allowed"}
            result= first_num/second_num
        else:
            return {"error":f"Unsupported operation '{operation}'"}
        return {"first_num":first_num, "second_num":second_num, "operation":operation, "result":result}
    
    except Exception as e:
        return {"error": str(e)}
    

@tool
def get_stock_price(symbol:str)->dict:
    """
    Fetch latest stock price for a given symbol (e.g. "AAPL", "TSLA")
    using Alpha Vantage with API key in the URL.
    """
    url= f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={os.getenv('STOCK_API_KEY')}"
    r= requests.get(url)
    return r.json()

tools= [search_internet, calculater, get_stock_price]

#**************************************** Groq model + tools access **************************************
model= ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key= os.getenv("GROQ_API_KEY")
)

llm_with_tools= model.bind_tools(tools)




#******************************************  Graph achitecture state**************************************************

class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage], add_messages]


#***************************************** Graph node fucntions **************************************

def chat_handle(state:ChatState):
    messages= [SystemMessage(content="You are question answering chat bot, and if you don't know about anything which is asked please tell that you don't know instead of telling irrelavent response"), *state['messages']]

    # prompt= ChatPromptTemplate.from_messages(messages)
    # parser= StrOutputParser()
    # chain= prompt| model|parser 

    result= llm_with_tools.invoke(messages)

    return {"messages":[result]}

# tools node 
tools_node= ToolNode(tools)


#************************************************ checkpointer + graph ***********************************************
# creating a database for checkpoint
conn= sqlite3.connect(database='./chatbot.db', check_same_thread=False) # so it will great that name database if there is not any database is created with that name 

# for checkpointer
checkpointer= SqliteSaver(conn=conn)



builder= StateGraph(ChatState)

builder.add_node('chat_handle', chat_handle)
builder.add_node('tools', tools_node)


builder.add_edge(START, 'chat_handle')
builder.add_conditional_edges("chat_handle", tools_condition)

builder.add_edge('tools', 'chat_handle')


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