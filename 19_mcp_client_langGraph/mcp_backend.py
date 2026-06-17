import os
import json
import asyncio
import aiosqlite
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
from langgraph.graph import StateGraph, add_messages, START, END
from typing import Annotated, TypedDict
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, SystemMessage, AIMessage, HumanMessage
from langgraph.prebuilt import ToolNode, tools_condition
from langchain.tools import tool
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
import sqlite3



load_dotenv()

DB_PATH= os.path.join(os.path.dirname(__file__), 'chatbot.db')

async def init_db(): # changed: add async
    try:
        # Changed: sqlite3.connect -> aiosqlite.connect
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("""
            CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount TEXT NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT DEFAULT '',
                note TEXT DEFAULT ''
            )
            """)
            await db.commit()
    except Exception as e:
        print(f"Database initialization error: {e}")
        raise

SERVERS={
    "math": {

        'transport':'stdio',
        "command": "C:\\Users\\Aditya Kumar\\AppData\\Roaming\\Python\\Python310\\Scripts\\uv.exe",
        "args": [
        "run",
        "--python",
        "3.12",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "D:\\Users\\Aditya_Kumar\\mcp_math_server\\main.py"
        ]
    },
}

model= ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key= os.getenv("GROQ_API_KEY")
)



async def main():
    await init_db()

    async with aiosqlite.connect(DB_PATH) as conn:
        # for checkpointer
        checkpointer= AsyncSqliteSaver(conn=conn)

        client= MultiServerMCPClient(SERVERS)
        # using this client we have to fetch all the tools present on local mcp server (math)
        tools= await client.get_tools() # list of tools

        model_with_tools= model.bind_tools(tools)



        class ChatBotState(TypedDict):
            messages: Annotated[list[BaseMessage], add_messages]


        # in asyncronus exicution all the node in the graph would be run asyncronusly
        async def chat_handle(state:ChatBotState):
            messages= [SystemMessage(content="You are question answering chat bot, and if you don't know about anything which is asked please tell that you don't know instead of telling irrelavent response"), *state['messages']]

            ai_result= await model_with_tools.ainvoke(messages)

            return {'messages': [ai_result]}

        # it is itself asyncronus
        tool_node= ToolNode(tools)

        builder= StateGraph(ChatBotState)

        builder.add_node('chat_handle', chat_handle)
        builder.add_node('tools', tool_node)

        builder.add_edge(START, 'chat_handle')
        builder.add_conditional_edges('chat_handle', tools_condition)
        builder.add_edge('tools', 'chat_handle')


        graph= builder.compile(checkpointer=checkpointer)

        config1= {'configurable':{'thread_id':1}}

        user_query= input("Ask!: ")

        result= await graph.ainvoke({'messages':[HumanMessage(content=user_query)]},config= config1)

        print(f"User: {user_query}")
        print(f"AI: {result['messages'][-1].content}")


if __name__=='__main__':
    asyncio.run(main())




# # creating a database for checkpoint
# conn= sqlite3.connect(database='./chatbot.db', check_same_thread=False) # so it will great that name database if there is not any database is created with that name 

# # for checkpointer
# checkpointer= SqliteSaver(conn=conn)


# @tool()
# def calculator(first_num:float, sec_num:float, operation:str) -> str:
#     """
#     Perform a basic arithmetic operation on two numebers.
#     Supported operations: add , sub, mul, div
#     """

#     if operation=='add':
#         result= first_num+ sec_num
#     elif operation=='sub':
#         result= first_num- sec_num
#     elif operation=='mul':
#         result= first_num* sec_num
#     elif operation=='div':
#         if sec_num==0:
#             return {"error": "Denominator can't be zeor!"}
#         result= first_num/sec_num
#     else:
#         return {"error":f"Unsupported operation '{operation}'"}
#     return {"first_num":first_num, "second_num":sec_num, "operation":operation, "result":result}

# tool_list= [calculator]





# model= ChatGroq(
#     model="meta-llama/llama-4-scout-17b-16e-instruct",
#     api_key= os.getenv("GROQ_API_KEY")
# )

# model_with_tools= model.bind_tools(tool_list)


# class ChatBotState(TypedDict):
#     messages: Annotated[list[BaseMessage], add_messages]


# def chat_handle(state:ChatBotState):
#     messages= [SystemMessage(content="You are question answering chat bot, and if you don't know about anything which is asked please tell that you don't know instead of telling irrelavent response"), *state['messages']]

#     ai_result= model_with_tools.invoke(messages)

#     return {'messages': [ai_result]}


# tool_node= ToolNode(tool_list)

# builder= StateGraph(ChatBotState)

# builder.add_node('chat_handle', chat_handle)
# builder.add_node('tools', tool_node)

# builder.add_edge(START, 'chat_handle')
# builder.add_conditional_edges('chat_handle', tools_condition)
# builder.add_edge('tools', 'chat_handle')


# graph= builder.compile(checkpointer=checkpointer)

# config1= {'configurable':{'thread_id':1}}

# user_query= input("Ask!: ")

# result= graph.invoke({'messages':[HumanMessage(content=user_query)]},config= config1)

# print(f"User: {user_query}")
# print(f"AI: {result['messages'][-1].content}")




