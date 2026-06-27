## Input and parameters are different things

## LLM memory -> A llm at inference is just a **Parameterized math function**

eg. y= f(x); y= ax^2 ; x-> input and a-> parameters; x-> input

- parameters are dicided by dataset ; when we try to fit our model to that dataset

- lly llm has billions of parameters

* so in llm output\* token= f\_(billions_of_params)(prompt_or_input_token)

* note: this mathematical equations are **stateless**

## A system is **stateless** if it's output depends only on the current input, and not on anything that happened before (bz parametes are fixed)

- so llm at inference time is stateless in nature

## It just means -> **Fact** - LLMs don't have any intrinsic Memory

- so we provide memory externally

## Context Window - The context window is the amount of text an LLM can read and remember at one time before answering. (that ability is context window for that llm) -> like screen of a camera feels like context window

- today's llm models context window is often to be 128K or greater tokens (roughly 200 pages pdf) ;; often its context window is big so we can take leaverage of that

* so context-window can help us to build memory of llm

## **In-context learning** - in an emergent ability that allows an LLM to use information and patterns present in the prompt itself, in addition to its trained parametric knowledge, to generate an answer.

- default way was that llm will answer using its parameteric knowledge, but in in-context learning llm also try to find pattern from the prompt itself (in-context learning) (eg RAG)

## so using Context-window and In-context-learning concept we can build a memory for llm

## how to implement short term memory in chatbot

- pick any chatbot there is concept of **converstation** -> (one session(short) with each conversation(thread))

* so each conversation has independent short term memory -> **STM is Thread scoped**

## Problems with STM

- 1. STM is fragile -> messages becomes blank after code reset/re-run ; solution use **persistant concept**

* means add STM+ database (before moving to any another thread save pre thread converstion)

* 2. The context window problem
* eg we are continue our conversation and message history become very big
* sol- >Trimming and summarization -> see **pic_1**

* 3. STM is thread-scoped

a) Loss of user continuity across conversations
b) Learning never compounds over time
c) Cross-thread reasoning is impossible

- like if we want to build -> personal assistant

* soluation -> we need a new kind of memory; which must have two kind of property

1. Information that should survive and 2. It has to be **selective** ;; see **pic_2**

- and these kind of memory in llm is called LTM (long term memory) bz it is mentening some important converstaion across the sessions

## Types of Long Term Memory

- Three types of Long-Term Memory (LTM) in LLM Systems ; See **pic_3**

## HOw does Long Term memory works?

1. Creation/updates
2. Storage
3. Retriever
4. Injection

## The Challenges

1. Deciding what is worth remembering
2. Retrieving the right memory at the right time
3. Orchestrating the entrie system

eg: external LTM memory which tell to focus on building your system the memory part will be done by it;; it works as memory layer
LangMem, Mem0, supermemory

- Google is building an transformer arch which will have their own memory -> paper => Titans+ MiRAS : helping Ai have Long-term memory
