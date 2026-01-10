## we will learn core concept of langGraph

## What is LangGraph

- LangGraph is an orchestration frameWork for building intelligent, stateful, and multi-step LLM workflows.

- It enables advanced featured like **parallelism, loop, branching, memory, and resumablity --** making it ideal for agentic and production-grade Ai applications.

- It models your logic as a **graph of nodes (tasks) and **edges**(routing) instead of a linear chain**

## 1. LLM workflows;;

- What is workflows -> **series of tasks** those we execute to achieve a our goal ;; so what is meaning of LLM workflows ---> there are some tasks in workflows which depends on LLM or use LLM

1. LLM workflows are a step by step process using which we can build complex LLM applications.

2. Each step in a workflow performs a distinct task -- such as prompting, reasoning, tool calling, memory access, or decision-making.

3. workflow can be linear, parallel, branched, or looped, allowing for complex behaviours like retries, multi-agent communication, or tool-augmented reasoning.

4. Common workflows

- a) prompt chaining (use when you have complex task and you want to divide into subtasks) and you can put **multiple checks** at maltiple places like here (gate) ;; eg may be like you want to build topic to detail report so for that you are building first **outline**(using LLM) and then give that outline to another llm to create detail report so this check point can check your outline should not be greater than 500 words;;

input-> LLM call 1 --output 1 --> Gate --if pass --> LLM call2 -- output 2--> LLM call 3 --> out \
 -- if fail --> Exit

- b) Routing (here you understand the tasks and decide which should solve this task (llm call router-> kind of decision maker))
- here query will **LLM call router** and it will decide what kind of this query is and then execute according LLM for that query
  ** see pic 2**



* c) Parallelization workflow-> here you break down given task in diff sub-tasks ;; and execute those at a time ;; merge there result and make final result ;; eg you are building an content moderation workflow for youtube (what is this? -> youtube check every content or video before public that is it good to public;; have to check same video from multiple angles;; eg 1. is that video follow youtube community guide linesd? , 2. do that video have any misinformation 3. sexual content )


* so here we have divided our content moderation workflow into 3 sub-tasks ;; so you can check these three things paralleli

* so what you will do;; you will send video transcript to all these 3 llm which will check these three things indivisually


* and these three llm will send there result to aggregator and this aggregator will decide is that contend follow those 3 rules or not or video should be publiced or not 


* d) Orchestrator Workers workflow;; lly like parallelization workflow

* task --divide --> parallel sub-tasks
* only diff is --> Orchestrator workflow -> you don't know behaviour of those llm before ;; it is dynamically dicide

* so there is **orchestratr** which decide what kind of search or work as to do those llm(workers) after analysis of the query ;; so this is main diff is that we don't know the nature of the task which will assign to the llm before, depending on the input query can be vary 
* see pic


* e) Evaluator Optimizer workflow ;; 

* here what happens you are given to a task;; problem with task is that you can't execute is once perfectly ;; like you want that your system draft a email for you ;; there is chance that you don't get perfect drafted email at first time;; lly you can ask for blog

* since these all works are on the basis of creativity;; so you need interation


* so here we have two kind of llm 1. Generator LLM and 2. Evaluator llm 

* you have told concrit evaluation criteria to that evaluator llm ; on the basis of that criteria it accept the generated blog or reject and with rejection it will also give you feedback; and evaluate except that blog then this loop will cloase and we will get the output




## 2. Graphs, Nodes and Edges

* The system generates an essay topic, collects the student's submission, and evaluates it in parallel on depth of analysis, language quality, and clarity of through. Based on the combined score, it either gives feedback for improvement or approves the essay.

1. Generate Topic
-> System generates a relevant UPSC-style essay topic and presents it to the student.

2. CollectEssay
-> Student writes and submits the essay based on the generated topic.

3. EvaluateEssay (Parallel Evaluation Block)
-> Three evaluation tasks run **in parallel:**
* EvaluateDepth -- Analyzes depth of analysis, argument strength, and critical thinking.
* EvaluateLanguage -- Checks grammar, vocabulary, fluency, and tone.

* EvaluateClarity -- Assesses coherence, logical flow , and clarity of thought.

4. AggregateResults
-> Combines the three scores and generates a total score (eg. out 15).

5. ConditionalRouting
-> Based on the total score:
* if score meets threshold -> go to **ShowSuccess**
* if score is below threshold -> go to **GiveFeedBack**

6. GiveFeedBack
-> Provides target suggestions for improvement in week areas.

7. CollectRevision (optional loop)
-> Student resubmits the revised essay.
-> Loop back to evaluateEssay

8. ShowSuccess
-> Congratulates the student and ends the-flow

* so node represent -> a single task --> behind the screen it is a python fn
* so we can think langGraph set of python fns and those are inter-connected with the help edges

* Edges tell us after execuation of one node task what whould be the next task;;

* nodes are telling what have to do , and edges tell when to execute a node 


## Through out this video we will se this Essay generator and evaluter workflow


## 3. State
-> In LangGraph, state is the **shared memory** that flows through your workflow -- **It holds all the data being passed between nodes as your graph runs.**

* eg;EssayWorkflow; state= {
  essay_text: str,
  topic: str,
  depth_score:int,
  language_score: int,
  clarity_score: int,
  total_score: int,
  feedback: Annotated[list[str], add],
  evaluation_round: int
}

* so this criticl component in langGraph ;; when you go to build any graph in langGraph, langGraph tells you first **define the state**

* benifity is that this state is accessible for each node in the langGraph (shared);; and each node make some changes in that state if needed then move it to there next nodes (mutable)

* so how to build this state --> this is a **Typed dict** (baiscally it is obj of typedDict class) ;; you can build a pydantic obj as well but mostly typedDict used


## 4. Reducers (closly connected with state concept)
* we know state is accessible(shared) and mutable(can changed its value by any node)

* and what happens multiple node can update same key's value ;; this often happens;; benfit is that we don't need diff key value for diff results;; this updating can be bad -> when we need previous results as well for next questions --> Eg: Chat-bot

* so that why we have **Reducer** ;; it tells how would this updating be done -> like you should replace or add or merge




-> Reducers in LangGraph define how update from nodes are applied to the shared state.

-> Each key in the state can have its own reducer, which determines whether new data replaces, merge, or adds to the existing value.

* eg;EssayWorkflow; state= {
  essay_text: str,
  topic: str,
  depth_score:int,
  language_score: int,
  clarity_score: int,
  total_score: int,
  feedback: Annotated[list[str], add], <-- **see we have specifically mentioned that feedback should be added in the list all the time**
  evaluation_round: int
}

* like here in Essay checker , if user get failed in evaluation process then the essay_text value will replace by it's new essay but if they again fail then the feed back will be added in the feedback list


* more often reducer is used in parallel workflow


## 5. LangGraph Execution Model (try to understand, behind the seen how langGraph execute a workflow)

* this execution model of langGraph is inspired by (google prgel) -> it's basically a system which can scale a graph in large scale

1. **Graph Definition** (so first we create a graph, so this whole process is called graph definition)
You define:
* The **state schema** (kind of typedDict)
* **Nodes** (functions that perform tasks)
* **Edges** (which node connects to which)

2. **Compilation** (try to understand the graph which you have build is structurlly good or not, like there should not a node which is not connected with any other node(orferned node))
-> You call `.compile()` on the `StateGraph` this checks the graph structure and prepares it for execution.

3. **Invocation** (pass the intial state to the first node that particular node will activate -> and partial update on our state, once this update is happend this updated state automtically passed to next node, and next node is automatically get updated and lly things will happens next;; and this step where we passing our state through edge to next node is called **message passing**)

* and this round by round works are called **super step** why super step why not only step -> due to some time use have parallel invokation ; and state is passed to each node and each node start running at the same time

-> You run the graph with `.invoke(initial_state)` LangGraph sends the initial state as a **message** to the entry node(s).

4. **Super-steps begin**
-> execution processds in **rounds**
-> In each round (super-step):
* all **active nodes** (those that received messages) run in **parallel**
* Each returns an **update** (message) to the state

5. Message Passing(through edges passing state to next node) and node Activation
-> The message are passed to downstream nodes via edges. Nodes That receive messsages become active for the **next round**

6. Halting condition
-> Executioin stops when:
* No nodes are active, and
* No messages are in transit


## one super step can have one or more than one steps









