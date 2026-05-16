import os
import requests
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from langchain_groq import ChatGroq

os.environ['LANGCHAIN_PROJECT']= "Agent"

load_dotenv()

search_tool= DuckDuckGoSearchRun()

# llm= HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct",
#     task="text-generation",
#     huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#     max_new_tokens=100,
# )

# model= ChatHuggingFace(llm= llm)

llm= ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key= os.getenv("GROQ_API_KEY")
)


# res= llm.invoke("hi")
# print( res)


@tool
def get_weather_data(city:str) -> str:
    """
    This function fetches the current wether data from the given city
    """
    return f"wether is very raining at {city}"



agent= create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful assistant. Be concise and accurate."
)

# What is the release date of Dhadak 2?
# What is the current temp of gurgaon
# Identify the birthplace city of Kalpana Chawla (search) and give its current temperature.

response= agent.invoke({"messages":[{"role":"user", "content":"Identify the birthplace city of Kalpana Chawla (search) and give its current temperature."}]})

print(response)