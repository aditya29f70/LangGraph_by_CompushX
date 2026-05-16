import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpointEmbeddings, HuggingFaceEndpoint
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable # <--- Key point ;; so by using it you can trace any function regardless of it is runnable or not


os.environ["LANGCHAIN_PROJECT"]= "RAG-V2"

load_dotenv()



llm= HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=100
)

model= ChatHuggingFace(llm=llm)


emb= HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)


# 1) load pdf

PDF_PATH= "islr.pdf"

@traceable(name='load_pdf', tags=['pdf', 'loader'], metadata={"loader":"PyPDFLoader"})
def load_pdf(name:str):
    loader= PyPDFLoader(name)
    docs= loader.load()
    return docs


# 2. splitter
@traceable(name="split_documents", tags=['splitter'], metadata={"splitter":"RecursiveCharacterTextSplitter"})
def split_documents(docs, chunk_size=1000, chunk_overlap= 150):
    splitter= RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    splits= splitter.split_documents(docs)
    return splits


# 3) embedding+ index
@traceable(name="build_vector_store", tags=['vector-store'], metadata={"vectorStore":"FAISS"})
def build_vector_store(splits):
    vs= FAISS.from_documents(splits, embedding=emb)
    return vs

# we can also trace a "setup" unbrella span if you want
@traceable(name="setup_pipeline")
def setup_pipeline(pdf_path:str):
    docs= load_pdf(pdf_path)
    splits= split_documents(docs)
    vs= build_vector_store(splits=splits)
    return vs


# Build the index under traced setup
vectorStore= setup_pipeline(PDF_PATH)
retriever= vectorStore.as_retriever(search_type='similarity', search_kwargs={"k":4})


# 4) prompt + chaning

def make_context(lis): return "\n\n".join(doc.page_content for doc in lis)

parallel= RunnableParallel({
    "query":RunnablePassthrough(),
    "context": retriever| RunnableLambda(make_context)
})


prompt= ChatPromptTemplate.from_messages([
    ("system","Answer ONLY from the provided context. If not found, say you don't know."),
    ("human","Query: {query} \n\nContext:\n{context}")
])

parser= StrOutputParser()


chain= parallel | prompt| model| parser


# 6) Ask questions
print("PDF RAG ready. Ask a question (or Ctrl+C to exit).")
q = input("\nQ: ")

config={
    'run_name':'pdf_rag_query'
}

ans= chain.invoke(q.strip(), config=config)
print("\nA:", ans)



