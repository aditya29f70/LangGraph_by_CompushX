* Create new frontend and backend files
* install http:pypi.org/project/langgraph-checkpoint-sqlite/ # so first install this library at backend side
* implement database in backend
* chat in multiple threads
* install and visualize 
* integrate to frontend



## there are three kind of checkpointer 
1. Inmemory saver (ram based)
2. sqlite saver ( generally use for prototyping)

-> so for that we have to install a library called -> langgraph-checkpoint-sqlite
-> after importing SqliteSaver, we have to create a sqlite database and connect to that sqlite checkpointer

-> why this -> 'check_same_thread=False' bz sqlite database has a problem that it works on single thread; so we are just trying to say we will be using this same database for different thread don't bother ; so it will not try to check different threads 

-> so it create different checkpoint in a thread according to what workflow we have designed (like here we have start, a node and end) so every query in a thread there would be three checkpoint for every query 

3. postgre saver