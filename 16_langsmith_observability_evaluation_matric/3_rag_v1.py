import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFaceEndpointEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough




os.environ['LANGCHAIN_PROJECT']= "RAG-v1"

load_dotenv()



llm= HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=100
)

model= ChatHuggingFace(llm= llm)

embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)


PDF_PATH= 'islr.pdf' 

# 1.) load pdf

loader= PyPDFLoader(PDF_PATH)

docs= loader.load()

# 2.) splite

splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
splits= splitter.split_documents(docs)


# 3.) Embed + index

vs= FAISS.from_documents(splits, embedding= embedding)
retriever= vs.as_retriever(search_type='similarity', search_kwargs={"k":4})


# 4) prompt 

# augmentation
parallel= RunnableParallel({
    "query": RunnablePassthrough(),
    "context":retriever| RunnableLambda(lambda x: "\n\n".join(rel_doc.page_content for rel_doc in x))
})

prompt= PromptTemplate(
    template="You are question-answer assistant. You have to answer the query: {query}.if you feel any external knowledge you can use this head content and answer query if you ensure there is answer other directly say you don't know :\n\n {context} ",
    input_variables=['query', 'context']
)

parser= StrOutputParser()


# 5.) chain
chain= parallel | prompt |model| parser


# 6.) ask questions
print("PDF RAG ready. Ask a question (or Ctrl+C to exit).")
q= input("\nQ: ")
ans= chain.invoke(q.strip())
print(f"\nA: {ans}")











