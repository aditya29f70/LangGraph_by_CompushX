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
