## It is kinds of fundational topic (bz there is lot of topic are build on top of it)

-> Persistance ; refer to ability to saved and restore the state of a workflow **overtime**

* What we have learnt (main objective) about langGrah
1. Concept of graph (defining nodes and edges)
2. concept state 

## we can build any complex workflow only using by these two concept of langgraph

## which maintaining state what were the problem we were facing
-> after invoke, state was erased . so we don't able to access what ever were inside it before , means in feature is we need those values we can't recover those state values; (core behaviour of langgraph)


## Using persistance we can change this behaviur 
-> so when we use persistance means; we can save our **state** somewhere after each invoke so in future we can see what the values inside our state and use it in future as well 

## 2. Now try to know about how exactly persistance works
* good thing about it that we don't only store final value of state it also store it all intermediates values

* Like let you have workflow (start -> node 1 -> node 2 -> end) and in state you have {"name":a} and let you change name value to b in node 1 and you also changing it value to c at node 2 but at the end persistance not only save it final value c but also save it all intermediate values like what was it value at intial state and node 1 and node2 defination you will see **overtime** term

* and due to that feature help a log
-> like you workflow crashed at node2 then if don't have persistance then name value would be its intial value what due to persistance bz it maintain state values at every timestop we will get 'name' value from it just previous node ;; so our workflow will not start from start now it can start from where it was crashed ;;; bz our **state is maintained till its just before node**  => that is a big features which is called -> **fault tolerance**

* in langgraph if persistance concept was not there than we can't get that **fault tolreance** like big feature


## 2 senario where persistance can help us

* building chat-bot ; bz you see that in any chatbot like feature you can carry you previous conversion from at we left it out


## we are telling that persistance store state every timestep but where -> a kind of **database**

## before moving in how to implement persistance in code , let try to understant some terms those are often used in persistance concept

## Checkpointers in Persistance

* note : in langgraph persistance was added due to checkpointer

* it basically devide out graph execution in checkpoints and at each checkpoints it basically save the state

## How checkpoints build ; in our graph each **super step** is made to a **Checkpoint**

## 3. Thread in persistance
* like it is used to distinues saving state things for different invoke bz in persistance they save state things again thread number which we give ;; so that why if we want to store things of another invoke state to different tread we can use it other wise all time when you click invoke state values are saved in a single thread ;; and if we want to retrieve some which only relevent to second invoke or like this we can to use different thread for that invoke

* very helpful ;; like you have build a chat bot and you want to maintain the conversion every time when use try to use it ; just use different tread id every time and if user want to resume any conversion where he left then we just find that thread id 

* we can resume all the things which in a tread id

# now implement
-> so we will provide a topic and a node will generate a joke and an another will generate an explaination and our workflow will end


## Benefit of persistence

presisly we get 4 benifits due to persistance 

1. we can implement **short term memory** in our chatbot 

2. we can have **fault toleranc** feature

3. we can implement **HITL** (human in the loop)

4. **Time travel** 

39: