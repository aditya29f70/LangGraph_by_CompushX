import os
import operator
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from pydantic import BaseModel, Field
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from langsmith import traceable

os.environ['LANGCHAIN_PROJECT']= 'LangGraph Eassy Evaluation'


load_dotenv()

#**************************** Model + Parser ****************************

# llm= HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct",
#     task="text-generation",
#     huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# model= ChatHuggingFace(llm= llm)

model= ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=os.getenv("GROQ_API_KEY")
)


class EassyOutput(BaseModel):
    feedback: str= Field(description="Detail feedback on the eassy")
    score: float= Field(description="score out of 10", ge=0, le=10)

struct_parser= PydanticOutputParser(pydantic_object=EassyOutput)
parser= StrOutputParser()



#******************************** LangGraph logic *************************

class EassyEvaState(TypedDict):
    eassy: str 
    cot_feedback:str 
    doa_feedback:str
    lang_feedback:str 
    eva_score: Annotated[list[float], operator.add]
    final_score: float
    summary_feedback:str




# we know langSmith **run** (traceing ) each node authmatically but we are also used traceable here explacitly for tracing whole function execution itself as well (what this whole function latency and information we are also interested to know)
# so this step is optional; we just want funciton level traceing as well 
@traceable(name='evaluate_clarity_of_thought')
def find_clarity_of_thought(state:EassyEvaState):
    prompt= ChatPromptTemplate.from_messages([
        ("system","You are an expert to find clarity of thought from a eassy"),
        ("user", "here is user written eassy: \n {eassy}. \nAnd you have to evaluate on the basis of clarity of thought and give feedback. Follow these output format instructions: \n\n {format_instructions}")
    ])

    prompt= prompt.partial(format_instructions=struct_parser.get_format_instructions())

    cot_chain= prompt|model|struct_parser

    result= cot_chain.invoke(state)

    return {"cot_feedback":result.feedback, "eva_score":[result.score]}

@traceable(name='evaluate_depth_of_analysis')
def find_depth_of_analysis(state:EassyEvaState):
    prompt= ChatPromptTemplate.from_messages([
        ('system',"You are an expert to find depth of analysis from a eassy"),
        ("user", "here is user written eassy: \n {eassy}.  \nAnd you have to evaluate on the basis of depth of analysis and give feedback. Follow these output format instructions: \n\n {format_instructions}")
    ])

    prompt= prompt.partial(format_instructions=struct_parser.get_format_instructions())

    doa_chain= prompt| model| struct_parser

    result= doa_chain.invoke(state)

    return {"doa_feedback":result.feedback, "eva_score":[result.score]}

@traceable(name='evaluate_language_understading')
def find_language_understanding(state:EassyEvaState):
    prompt= ChatPromptTemplate.from_messages([
        ("system", "You are an expert to understand eassy language"),
        ("user", "here is user written eassy : \n {eassy}. \nAnd you have to evaluate on the basis of language understanding. Follow these output format instructions:\n\n {format_instructions}")
    ])

    prompt= prompt.partial(format_instructions=struct_parser.get_format_instructions())

    lang_chain= prompt| model|struct_parser

    result= lang_chain.invoke(state)

    return {"lang_feedback":result.feedback, "eva_score":[result.score]}


@traceable(name='summary_feedback')
def final_score_and_summary_feed(state:EassyEvaState):
    final_score= sum(state['eva_score'])/len(state['eva_score'])

    prompt= ChatPromptTemplate.from_messages([
        ("system", "you are an expert eassy feedback summarizer."),
        ('user', "you have to summaries these three feedbacks 1. clarity of thought:{cot_feedback}\n2. depth of analysis:{doa_feedback}\n 3.language feedback:{lang_feedback} \n\n for eassy : \n {eassy}")
    ])

    summary_chain= prompt|model| parser

    result= summary_chain.invoke(state)

    return {"final_score":final_score, "summary_feedback":result}





builder= StateGraph(EassyEvaState)

builder.add_node('cot_', find_clarity_of_thought)
builder.add_node('doa_', find_depth_of_analysis)
builder.add_node('lang_', find_language_understanding)
builder.add_node("summarizer", final_score_and_summary_feed)


builder.add_edge(START, 'cot_')
builder.add_edge(START, 'doa_')
builder.add_edge(START, 'lang_')
builder.add_edge('cot_', 'summarizer')
builder.add_edge('doa_', 'summarizer')
builder.add_edge('lang_', 'summarizer')
builder.add_edge('summarizer', END)

graph= builder.compile()


Eassy= """
Mahatma Gandhi, popularly known as the 'Father of the Nation', holds an esteemed place in India’s history. Born on 2nd October 1869 in Porbandar, Gujarat, Gandhi grew up in a family that valued honesty and simplicity. After studying law in England, he practiced as a barrister in South Africa, where he first encountered and challenged racial injustice.
Gandhi returned to India in 1915 and soon emerged as a prominent leader in the freedom struggle against British colonial rule. He introduced revolutionary yet peaceful methods such as Satyagraha (truth-force) and Ahimsa (non-violence), believing that truth and non-violence were more powerful than weapons. Major movements led by Gandhi include the Non-Cooperation Movement (1920), Salt March (Dandi March, 1930), and the Quit India Movement (1942), which united Indians across caste, class, and religion.
A champion of equality, Gandhi also campaigned against social evils like untouchability and promoted Swadeshi (use of Indian-made goods). His lifestyle—wearing khadi, practicing vegetarianism, and leading by personal example—became a source of inspiration not only to the nation but to the world. Leaders like Nelson Mandela and Martin Luther King Jr. adopted his philosophy in their own movements.
Gandhi’s teachings remain relevant in 2025 as the world continues to value peace, justice, and sustainable living. His legacy is celebrated on 2nd October every year as Gandhi Jayanti and the International Day of Non-Violence. Gandhi’s life offers valuable lessons in honesty, resilience, and the transformative power of peaceful protest. His ideas empower today’s youth to build a more compassionate and unified society.
"""

config= {
    "run_name":"evaluation_upsc_essay", # becomes root run name
    "tags":["essay", "langGraph", 'evaluation'],
    "metadata":{
        "essay_length":len(Eassy),
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "dimensions":['language', 'analysis', 'clarity']
    }
}


result= graph.invoke({'eassy':Eassy}, config=config)

print(result)








