## What are subGraphs?

-> A subgraph in LangGraph usually means a graph that is embedded and executed as a node inside another graph.

## why subgraph are needed?

-> when we work on a problem which can be seperated into different independent sub parts/graph to work on so this safe our workflow to become large workflow (sigle big state) where each subgraph works independently on a particular task bz it is possible that each subparts/graph contains such good tasks itself like

- Tool calls, RAG, Conitional routing, Retries, Memory, HITL, Evaluation, Guardrails

* Bz genAi problem can be complex so we have to make it simple by splitting multiple graph (each can have it won agent working and evaluation methods)

## So what we achieved by doing it

-> modularity
-> re-usibilty
-> maintainbility (if bug come we can know from where it was arrised )

- langgraph specific benifit
  -> Failure Isolation (like if any subgraph faces issue then will not affect other subgraph , others will run)
  -> state separation (each subgraph will have its own state, so state will not be mismatched)
  -> Observability (langSmith gives ability to trace a single subGraph)

## Now it time to implementation of both types subGraph

1. first type -> add a subgraph in parent graph (both graph will have there own state)

- parent graph; -> start-> generate -> translate(here we will just invoke the subGraph) -> end
- subGraph; -> Start -> Trans -> end

## please go through there are lot of good things like

-> how langgraph maintain persistance across parent and subgraph
-> how to see subgraph state etc
