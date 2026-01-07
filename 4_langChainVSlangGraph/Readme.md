## Goal

1. Why LangGraph exists? (why we can't add those things in langChain to build agentic model)
2. What is LangGraph?
3. LangChain vs LangGraph (when to use what)

- imp thing about langChain is langchain has **Chain** concept;

- What you can build using LangChain

1. Simple conversation workflows like Chatbots, Text Summarizers

2. Multistep workflow

3. RAG application

4. Basic level agents

## now we take some complex workflow (automated hiring , which we have disscussed before) and try to things why LangGraph;; first try to build it using langChain and analys what exactly problems are there

- see the **pic-1** working flow of hiring manager agentic ai

- this workflow is not agentic ai application (sir told) instead it is a workflow

- now what is diff bw Agentic ai applicaiton and workflow you have to go **Anthropic blogs** and try to read this blog **Building effective agents**

- **WorkFlows** are systems where LLMs and tools are orchestrated (at which step, which tool has to be called) through predefined code paths;; it is fixed and made by devloper that by it is not agentic;; you run one time or any number of time flow would be same

- **Agents**, on the other hand, are systems when LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.;; here all the steps are executed automatically (decided by llm )

## start (see pic-1(s))

- request -> so we said we need backend engineer , job would be remote and have 2-4 years of experience
- asked to create a jd and tell human to check if they like then move to post other wise take human feedback and run that loop again
- now post the jd using tool callig let we have tools access like (linkedin and nakuri);; now we have fixed that it has to wait 7days ; so after 7days
- now our system check **monitor applications** how many students have applied using tool called (call linkedin api call)
- now asking that **do we have enough application** so we have decided some thresold before so according to that if we have that number of applicat then start shorlisting , scheduling conduct interview etc otherwise modify Jd and wait 48 hour and move to that loop again (monitor application)

- so for shortlisting we can use call Resume parser tool to get ats score for there resume and on the basis of those score we can select let 5 of them now we have to take interview for them so we call calender or mail to send or schedule for interview and conduct interview so for that we send some interview questions to conductors and send time to take interview etc

- and after that we will ask question to interview conductor are the selected or not if no them send email to them if yes then send offer letter

- now we wil be tracking have those applicatent selected the offer later or not
- if yes then send onbording if no then re-negotiate(done by humum) start loop (send offer later again)

## now we have to code this work flow using langChain

- this a complex work flow

- now discuss point-by-point note that if we go to solve this problem using langchain then what diff kind of problem we will be facing;;


## Callenges:
1. Control flow complexity

* Chains has linear workflow;; but our workflow is highly nonlinear why (at which basis it is highly nonlinear)

* * 1. conditional branches (that why nonlinearity coming)
* * 2. loop
* * 3. at multiple places we have **jumps** (suddently you go back(muiltiple step back))

* now we try to make program in langchain only for start to **post JD**

* problems (see the code in 1_hiring):
-> langchain doesn't give loop kind of fasility , there i used python loop and custom fn for approval from human (that is currently dummy fn)

* note: **when ever you write code by yourself without using that lib where we was working  ;; in order to steach the entire flow that code is called -> Glue-code ;; and less glue-code is good for sys; always try to use less or no glue code

* but in out system there are lot of glue code possible withoug it we can't build it

## so conclusion -> langChain doesn't have that kind of constractor to build complex workflow (like conditional branching, loop, jump) 
-> so you have to build it using pytho(**Glue-code**) when you go to build complex workflow by langchain --> due to glue code its maintainbility will reduce

## so langchain work great for linear kind of workflow not for complex workflow


## how will approch this workflow if we will go to build it using langGraph

1. first you represent your whole workflow as **graph**
* in graph represent each task as node and drow edges so with help of it control flow 

* since we are drowing it as graph and graph is non-linear data structure ; so we can drow any kind of complex workflow in langGraph and solve

eg.\
`graph.add_node("HiringRequest",hiring_request) \n
graph.add_node("CreateJD", create_jd) \n
graph.add_node("CheckApproval", check_approval) \n
graph.add_node("PostJD", post_jd)`

`graph.add_edge("HiringRequest", "CreateJD") \n
graph.add_edge("CreateJD", "CheckApproval") \n

graph.add_conditional_edge(
  "CheckApproval",
  approval_router,
  {
    "approval":"PostJD",
    "not_approved":"CreateJD" ##looping back
  }
)
`

* note ; here you don't need to write anything in custom python;; we don't need to write python for loop, jump, condition ;; for all these things we have pre build features in langGraph

* so in langGraph
* each tasks become **node**
* each control flow done by **Edges**
* and we can apply loops on the edges or can apply any condition/branching on these edges


## (2nd) Challenge : Handling State
* What is concept of **State** in complex workflow
-> for this control flow works correctly we should have a state of it where we have mentioned all the import task have been done or not and send this state after each task

* and state all being changed bz it is that things which moving for control flow and get updated

* and with help of this **workflow-state** system can understand what we have done and what we have to do next

* this **State** exsist as key-value pairs

* and langChain doesn't key to store and track such key-value pair

* LangChain has memory concept what that is **Conversional memory** -> (we store chating which we have done before with llm) and can send it anywhere 

* so langchain is state-less;; if you want this state in langChain then you have to build it manually ;; you have to put all the key value in that dict and manually have to update after each task.

* How langGraph handle this challenge
-> LangGraph is state-ful
-> when you create **graph** in LangGraph at the same time you create **State Obj**(you can build using pydantic or typedict not problem)

* and good thing is that it is accessiable by all the node in the graph ( and this state-obj is mutable so these node can change its value)

* and changes can be visible by very node in state

## (3) Challenge : Event driven Execution. 
* What is that?
* when ever you build a workflow simple /complex that can execute by two ways

1. squencial (for eg you can take a squencial LangChain pipeline where you can thing you chain component output directly go as input of next component without stopping or waitting of any response)
2. Event driven (but here the chain can stop at any point for a external or internal response untill it will not move further steps) or you will have to wait of something is triggered;;
* eg in hiring sys;; after jd posting system have to wait or pause the work flow for 7 days after that it can monitor the applications

* Langchain is not build of Event driven , it is build for sequencial execution ;; if you go with langchain you have to again write lot of glue-code ;; which is not good

* what you can do in LangGraph you can saved you state using (Checkpointer) before that 7 days pause, and after that you can pause and waiting for external trigger;; and when you get external trigger you see your current state and start running things with same state which it have gotten

## (4) Challenge : Fault Tolerance (if some thing bad is happened with syster after that can that sys run or not) --> good for those workflow which is **Long-running (7 days + 48hr waitting possible)** that why fault changes are very high

* Fault can be two type
1. Small fault (an simple node problems)
2. Big fault (server is down where you have deployed)

* ideally -> there would be that kind of sys which can recover from both of the faults

* langChain does't have **Fault Tolerance** concept means at where system is crashed it will resum from at that same point ; but langChain restart thing if it fail at any point 

* langGraph have build-in **Fault Tolerance**
* langGraph gives fault tol. at both of the cases small fault(give option retry logic on that node) and big fault or system lever fault (it has recovery concept;; like you was at any node and server lost so langGraph give you a option that you can resume the flow from the same node;; Checkpointer-concept used)

* since this whole execution is stateful (every time tracking state and saveing in memory or in external database(persistence layer));; what you langGraph does it make checkpointer after each node execution and take a copy of the state in memory;; so with help of that checkpoint you can resume things at that pause point node


* so **Fault Tolerance is high of LangGraph**


## (5) Challenge - Human in the loop;;

* so langChain does't have any such feature where it can pause for human response and run ahead after getting a response from human

* you can do it by langChain you can divide you chain into two part according where you want to ask question to human run the first chain and wait for human response then accordingly run sencond chain, note you have to manually send the state to the second chain if you have with langChain


* but in LangGraph **Human in the loop** is  **First class citizen**

## (6): nested WorkFlows

* LangGraph has a features where you can replace a single node of it to a diff whole graph 

* esencially you can plot subgraphs/ you can make nested workflows

* we will study that main graph has their own state and output or subgraph has their own state how they interect .

* it's two major use cases
1. You can build **MultiAgent system**
2. using SubGraph you can enter Reusablity in the Picture or you can make a graph as reusable ;; like you can use it at diff parts of a graph 


## (7) Challenge - Observability
* Observability refers to how easily you can monitor, debug, and understand what your workflow is doing at runtime.

* this observability concept we get in langChain as well ;; for that we have **Langsmith(exactly same purpose)-> it monitor llm based application** 

* you can easly integrate **LangSmith** to you langChain

* it record every thing talk with llm to what it's response etc

* there is a problem that -> LangSmith can only monitor langChain ;; can't monitor your **Glue-code** ;; and we have seen that when you go for complex workflow with langChain you have only way to Glue-code at multiple places


* so in that case langsmith will get partial observability


* that prob can be easly solved by LangGraph
* LangGraph has tight integration with LangSmith
* langGRaph tell very things to langSmith


## LangGraph Handle **workflow orchestration**. while LangChain Provides the **building blocks** for each step in that workflow

## see pic_3

