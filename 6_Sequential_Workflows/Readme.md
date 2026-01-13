# Will learn how to make sequencial workflow in langGraph

-> see basic code how to write in langGraph
-> so after that we can build any kind of sequencial workflow

- now first we have to install the langGraph

## we will use jupyter notebook --> bz by using jupyter notebook we can draw the graph of langGraph

## First workflow (not llm workflow) simple workflow --> bmi calculater workflow

- we will send input(as height+ weight) --> send to a node (where we will calculate bmi) --> output (result)

- since we will do it by langgraph so for that we will draw graph for that ;; and have to define **state**
- three key-value pairs will be in our state --> weight, height, bmi


## now let try to build LLM workflow (try to understand how langChain and langGraph work hand-to-hand)
## simple START -> llm_qa -> END

* LLM_qa -> take query from state ask to llm get answer from llm and put it in state


## now from common workflows let try to build first of them -> **prompt chaining** -> call multiple llm in series

* now about llm workflow -> we will provide a topic  --> llm will generate a blog

* this workflow is prompt chaining bz we will not generate blog directly from topic instead what we will do

* first we will give this topic to a llm and tell to generate a outline ;; once this outline is generated then after we again go an llm and tell for this topic + outline -> generate the blog -> final blog

* topic -> llm (tell generate outline) -> LLM (give topic+ outline and tell generate blog) -> blog

* START -> Generate outline -> Generate blog -> END

* Why this is prompt chaining -> bz there is two node and in both we are interecting with llm (in prompt chaining basis -> we interect llm multiple times)


## Think if we are gonna solve this using langChain so we have to use ParallelRunnable two time to get such kind of structured out that langGraph gave (type dict with topic, outline, blog;; this is happened bz we have state concept in langGraph which evalave each super step)