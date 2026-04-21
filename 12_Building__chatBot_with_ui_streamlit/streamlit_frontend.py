import streamlit as st
from langgraph_backend import config1, graph
from langchain_core.messages import HumanMessage




# with st.chat_message('user'):
#     st.text('Hi')


# with st.chat_message('assistant'):
#     st.text("How can i help you?")


# user_input = st.chat_input('Type here')

# if user_input:
#     with st.chat_message('user'):
#         st.text(user_input)






# we have to maintain message history like
# {'role':'user', 'content':'Hi'}
# {'role':'Ai', 'content':'Hello'} etc and store these into python list

# message_history=[]

# ideal we should have that dic which don't resent after re-run the whole page -> affortunitly we a such dict -> streamlit has -> st.session_state = it is dictionary but don't erase after enter
# resent only when we manually refers the page 

# checking is this first step where we don't have any message_history attr in st.session_state
if 'message_history' not in st.session_state:
    st.session_state['message_history']= []

# loading the conversation history 
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


# taking user input 
user_input= st.chat_input("Type here")

if user_input:

    # for user response
    st.session_state['message_history'].append({'role':"user", 'content':user_input})

    with st.chat_message('user'):
        st.text(user_input)
    


    ai_res= graph.invoke({"messages":[HumanMessage(content=user_input)]}, config=config1)['messages'][-1].content

    # for assistant response
    st.session_state['message_history'].append({'role':"assistant", 'content':ai_res})
    with st.chat_message('assistant'):
        st.text(ai_res)



