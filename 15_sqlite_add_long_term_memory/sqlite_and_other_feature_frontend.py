import streamlit as st
from sqlite_backend import graph, retrieve_all_thread_ids, checkpointer
from langchain_core.messages import HumanMessage, AIMessage
import uuid


# ********************** utility functions *****************************

def generate_thread_id():
    thread_id= uuid.uuid4()
    return thread_id

def new_thread_and_reset():
    new_thread= generate_thread_id()
    st.session_state['thread_id']= new_thread
    st.session_state['message_history']= []

    st.session_state['thread_history'].append(new_thread)


def load_conversation(thread_id):
    config= {'configurable':{'thread_id': thread_id}}


    if 'messages' in graph.get_state(config=config).values:
        messages= graph.get_state(config=config).values['messages']
    else:
        messages= []

    temp_messages=[]

    for message in messages:
        role=None
        if isinstance(message, AIMessage):
            role= 'assistant'
        if isinstance(message, HumanMessage):
            role='user'

        if role:
            temp_messages.append({'role':role, "content":message.content})
        

    return temp_messages




def change_thread(thread_id):
    st.session_state['thread_id']= thread_id
    # now ask to our backend memory to give that thread_id message history (don't need to save in steamlit state history )
    st.session_state['message_history']= load_conversation(thread_id)


def generate_thread_message(thread_id):
    config= {'configurable':{'thread_id': thread_id}}

    if 'messages' in graph.get_state(config=config).values:
        messages= graph.get_state(config=config).values['messages'][0].content
    else:
        messages= []

    if messages!=[]:
        msg= " ".join(messages.split()[:8])
    else:
        msg= f"{thread_id}"

    return msg



# *******************sesssion setup ************************************
if "message_history" not in st.session_state:
    st.session_state['message_history']=[]

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']= generate_thread_id()
    st.session_state['thread_history']= retrieve_all_thread_ids(checkpointer)+ [st.session_state['thread_id']]


# ******************** Sidebar UI **************************************

st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    new_thread_and_reset()

st.sidebar.header('My Conversations') 

# show all thread_id with click button so they can select their previous conversation
for thread_id in st.session_state['thread_history'][::-1]:
    if st.sidebar.button(f"{generate_thread_message(thread_id)}"):
        change_thread(thread_id)


# st.sidebar.text(st.session_state['thread_id'])


# ************************* Main UI **************************************

CONFIG= {'configurable':{'thread_id': st.session_state['thread_id']}}

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input= st.chat_input('Type here')

if user_input:

    st.session_state['message_history'].append({'role':'user', 'content':user_input})

    with st.chat_message('user'):
        st.text(user_input)

    # ai_message= graph.invoke({'messages':[HumanMessage(content=user_input)]}, config=config1)['messages'][-1].content

    stream= graph.stream({'messages':[HumanMessage(content=user_input)]}, stream_mode='messages', config=CONFIG) 
    # stream= generator

    # go to streamlit document you will see it has a build in function write_stream and where we only need to give our generator

    with st.chat_message('assistant'):

        ai_message= st.write_stream(message_chunk.content for message_chunk, metadata in stream)

    
        # we also store response in a variable so once it has been done to write it 
    
        st.session_state['message_history'].append({'role':"assistant", 'content':ai_message})

    st.rerun()


    # st.session_state['message_history'].append({'role':"assistant", 'content': ai_response})
    # with st.chat_message('assistant'):
    #     st.text(ai_response)