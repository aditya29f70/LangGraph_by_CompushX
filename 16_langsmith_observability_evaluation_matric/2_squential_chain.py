import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough


os.environ['LANGCHAIN_PROJECT']= "Sequential LLM App"

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=100,
    repetition_penalty=1.5,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)


model= ChatHuggingFace(llm= llm)


prompt1= PromptTemplate(
    template="Generate a detailed report on {topic}.",
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template="You are a report-summarizer and you have to summaries report: \n {report} \n which is created on topic: {topic} ",
    input_variables=['report', 'topic']
)


parser= StrOutputParser()


topic_gen= RunnableParallel({
    "topic":RunnablePassthrough(),
    "report":prompt1 | model | parser
})

summary_gen= topic_gen| prompt2| model|parser

# we can give our favarate meta-data and tag
config= {
    # "run_name":"sequential_chain",
    "tag":['llm app', 'report generation', 'summarization'],
    "metadata":{'model1':"meta-llama/Meta-Llama-3.1-8B-Instruct", "parser":'stroutputparser'}
}

result= summary_gen.invoke("dragon", config=config) # {"topic":"dragon"} ;; not sending this bz RunnablePassthrough directly take that dict not topic (dict in str format)

print(result)




