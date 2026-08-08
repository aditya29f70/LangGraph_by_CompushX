# In the lec will see how to implement STM in langgraph

-> persistance concept
-> at the last work on context window problem (will understand diff technics such as )
--> trimming
--> deletion
--> summarization

- llm is stateless (means very time when we invoke llm it forgates its all previous conversation) -> so **conversation buffer** comes in picture

* so in langgraph **checkpointer**(we save our state anywhere after every super step) + **tread id** helps to implement STM internally

## we know how to implement STM using 'Inmemory saver'

- and for persistance we can use database for long term persistance (like postgre)
- there are two ways to use postgre

1. postgre in our own machine -> langgraph will use (in this way lot of installation related issues come so will use below sec way )
2. docker -> postgre -> langgraph

- we will follow second way
  -> we will install postgre using docker and then langgraph will use that setup to interact with database

## Steps

1. Install Docker -> `http://www.docker.com/products/docker-desktop/`
2. Launch docker desktop
3. Check if docker is already installed -> docker -> version
4. create docker-compose.yml
5. docker compose up -d # to run that docker compose
6. docker ps -> to check whether that docker compose is running or not
7. install python dependencies (just need to install some python dependencies)

```
!pip install -U\
    langgraph\
    langgraph-checkpoint-postgres\
    psycopg[binary, pool] \
    langchain-openai \
    langchain-huggingface
```

## so you can see using this method we are able to persist our state

## now lets discuss about **\*\*\***'Context overflow problem'\***\*\*\*\***

- context window of llm is a space which tell how many max token can be processed by that llm at a time

- so in **STM** there is high chance of 'context overflow problem' bz in each human question we are adding all pre convesation his with it

## solutions

- triming -> here we setup max_token_limit;; so that messages we sent to llm , now we will count token size of messages and make sure its size should not cross limit (manual way) if it cross the limit we do triming

* we will add layer trimming before sending messages to llm ;; so we wil take only **last n-messages whose token counts come up to max token size**
* vvimp -> we are not actually deleting the messages here , those messages will be persist in the memory

* and you can also able to see what is problem with trimming; -> since it takes only last n-messages whose token size don't cross limit ; so there is chances that it will take only currently response only if adding single pre message cross token limit

* So summarization comes into picture

## Summarization

- we use it with trimming bz we know in trimming it takes top N messages according to what max_token we have fixed ;; so for rest messages can also be very useful or having context for current question so we take summary for those rest messages so for creating summary we send those rest messages to LLM and ask to generate a summary for them

* now we send a combination of those **trimmed N messages** and **summary** to llm
* after generating summary of rest messages, we **delete** them (not ignore , completly delete from state) bz there is not any sence to carrying those messages as well there summary

* so first need to understand how deletion works
