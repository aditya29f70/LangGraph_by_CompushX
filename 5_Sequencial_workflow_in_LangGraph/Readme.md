## we will learn core concept of langGraph

## What is LangGraph

- LangGraph is an orchestration frameWork for building intelligent, stateful, and multi-step LLM workflows.

- It enables advanced featured like **parallelism, loop, branching, memory, and resumablity --** making it ideal for agentic and production-grade Ai applications.

- It models your logic as a **graph of nodes (tasks) and **edges**(routing) instead of a linear chain**

## LLM workflows;;

- What is workflows -> **series of tasks** those we execute to achieve a our goal ;; so what is meaning of LLM workflows ---> there are some tasks in workflows which depends on LLM or use LLM

1. LLM workflows are a step by step process using which we can build complex LLM applications.

2. Each step in a workflow performs a distinct task -- such as prompting, reasoning, tool calling, memory access, or decision-making.

3. workflow can be linear, parallel, branched, or looped, allowing for complex behaviours like retries, multi-agent communication, or tool-augmented reasoning.

4. Common workflows

- prompt chaining (use when you have complex task and you want to divide into subtasks) and you can put **multiple checks** at maltiple places like here (gate)

input-> LLM call 1 --output 1 --> Gate --if pass --> LLM call2 -- output 2--> LLM call 3 --> out \
 -- if fail --> Exit

- Routing (here you understand the task and decide which should solve this task (llm call router))
- here query will **LLM call router** and it will decide what kind of this query is and then execute according LLM for that query
  ** see pic 2**
