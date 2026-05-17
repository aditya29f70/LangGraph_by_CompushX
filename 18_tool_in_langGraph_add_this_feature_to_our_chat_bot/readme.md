## we are planning to add three tools

1. give calculater tool capability
2. internet search
3. stock tool; (give companey name it will return that companey stock price)

- so first try to see how to use in langGraph and then after add these three features in our chat-bot

## **Tools conditions** which is used inside chat_node ; which is basically helps us to know model want to call tools or general talk

- what technical here we are directly giving tools output , nothing policing on it structure data; why in real world we want polic text which telling what tools output summary
- or we sould return back tools output to llm so it will decide to call another tools on the basis of output or just return a polic output

## now we have learnt how to add tools concept in langgraph now add these three tools fasility to our chat-bot

- see the observability_implemented chat-bot i have implemented there ;it is just before it

* i also tried to show what kind of tools it is using during resoning -> go streamlit site -> **chat elements**
* there are 4 chat elements ; 1. st.chat_input, 2. st.chat_message('user') , 3. st. status, 4. st.write_stream
