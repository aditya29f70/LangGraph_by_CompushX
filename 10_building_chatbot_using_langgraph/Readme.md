## we are gonna build a chatbot by which we will try to add-> chatting , RAG, Tools, UI, Langsmith;; duing building the chatbot we will try to understand some advance topic of RAG(memory concept, persistance, check-pointers, Hitl, retry(folt torance) );; we will be contributing things in it

- first try to understand it design -> (essencially chatbot has a llm based workflow)
- so user ask question -> llm reply it and then user can ask and we have to implement this loop

* state would be -> messages (that user and llm message history)

## What is the problem here, the memory -> here we are invoking it again-and-again , we are not maintaining any kind of memory , for that we should be a such kind of workflow in which a looping will be happened then it can get a state which basically contain the previous conversation

- i meant that when ever you call invoke , it just means you doing things from scratch again or you state will initalize from empty

## for resolving it we use a concept which is called -> **persistance**

- for now we are gonna use it only

* what happens generally -> when we go from Start -> End we initalize our state and at the end we retrun it and new time we invoke we loss our previous state

## what we do in persistance -> when our exicution reach at then end -> we don't erase instead we store it somewhere

- we have multiple option to store it

1. Only database (in industry we use it)
2. Store in Ram (like when ever our program is running states things will be stored) (since we are building basic level chatbot we use Ram base memory)

## for that you have to import from langgraph.checkpoint.memory import MemorySaver (this is kind of memory in langgraph, which store things in ram)

- now build a checkpointer which is a object of MemorySaver
- and at the point where you compile you graph you tell about your checkpointer (so we have told that in our graph we also have a checkpointer, and that checkpointer is kind of memorySaver)

- now we have to do a things when we invoke a workflow -> 1. have to define a thread (what it means one interaction with chatbot, it tells -> chat is live) (so we provide a id to our thread so we can identify it , thread_id="1")

- like me when we interact with thread which will happen on one thread, any other person can also interact with the chatbot but their thread will be diff

- 2. when you are gonna interact with chatbot, you just define **config** variable , and it is dictionlary and it has a key **configurable** and it's values also be a dict with key **thread_id** and value that thread_id which we have decided

- 3. now while invoking our chatbot, we will not only give our messages but also give that config variable

## now what happening , so our conversation is not get erased at the end , we are stroing those whole conversation in our ram memory and every invoke

## our model is getting whole coverstion ;; or in our state the whole conversation are being stored

- how this happens -> at the end of first invoke we have our final state ->put it in the ram -> in next invoke langgraph take the state from the ram memory and append the new state messages (bz we have using **add_messages** reducer fn), it don't only start with a new state -> and some things happen in further conversation
