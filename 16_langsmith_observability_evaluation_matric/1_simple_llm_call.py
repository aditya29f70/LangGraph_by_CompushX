import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm= HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=100,
    repetition_penalty=1.5,
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm=llm)

prompt= PromptTemplate(
    template="You are a question answering assistant and answer user query if you know other-wise directly said you don't know about that. User query is : {query}.",
    input_variables=['query']
)


parser= StrOutputParser()

ChatModel= prompt|model|parser

result= ChatModel.invoke({"query":"What is the capital of peru?"})

print(result)