import streamlit as st
from backend import config1, graph
from langchain_core.messages import HumanMessage


if "message_history" not in st.session_state:
    st.session_state['message_history']=[]


for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input= st.chat_input('Type here')

if user_input:

    st.session_state['message_history'].append({'role':'user', 'content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # ai_response= graph.invoke({'messages':[HumanMessage(content=user_input)]}, config=config1)['messages'][-1].content

    stream= graph.stream({'messages':[HumanMessage(content=user_input)]}, stream_mode='messages', config=config1) 
    # stream= generator

    # go to streamlit document you will see it has a build in function write_stream and where we only need to give our generator

    with st.chat_message('assistant'):
        ai_message= st.write_stream(message_chunk.content for message_chunk, metadata in stream)
        # we also store response in a variable so once it has been done to write it 

        st.session_state['message_history'].append({'role':"assistant", 'content':ai_message})


    # st.session_state['message_history'].append({'role':"assistant", 'content': ai_response})
    # with st.chat_message('assistant'):
    #     st.text(ai_response)