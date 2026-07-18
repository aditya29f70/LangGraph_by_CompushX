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
