import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task="text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)


hiring_prompt= "We need to hire a software Engineer for our Backend team."


# step2; create jd using LLM
jd_prompt= PromptTemplate(
  template="Create a job description based on the hiring request:\n\n {request}",
  input_variables=['request']
)


jd_chain= jd_prompt | llm | StrOutputParser()

# step3: Approval fn

def approve_jd(jd:str) -> bool:
  # Simulate approval logic
  return "Approved"

# step4 : post JD fn

def post_jd(jd:str):
  print("JD Approved and posted:\n")


# step5: loop untill JD is approved

approved= False 
jd_output= None

while not approved:
  jd_output= jd_chain.invoke({"request":hiring_prompt})
  print(jd_output)

  approved= approve_jd(jd_output)

  if not approved:
    print("JD not approved. Regenerating .... \n ")

# final step:
if approved:
  post_jd(jd_output)