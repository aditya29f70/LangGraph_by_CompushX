## Try to know what is MCP (Modern context protocol) and why we need it -> we can say MCP is a improved version of tools bz tools has a inheritent flaw that why mcp comes in the picture

- so it is not a new things , it just a new way to integrate tools with our chat-bot or llm application
- or mcp is a standard way to integrate tools with our llm application;

## Problem with tools

- mcp is inhence version of tools (bz teditional tools connection had some issues)

* it had tools access like web-search, calculator and get stock price
* now i want to connect our chat to git-hub copilate so we can ask about our repos(bz we want to build that chatbot for our company develaper team)

* langchain does have any pre-build github tool, we have to build that tool(custom tool)
* build a tool where we can ask for how many pr i made on that rep

## today's class we will try to build our own mcp client using langGraph

## note: we can use mcp server as well as tools both at a time

## when problem arries when we go to build mcp client, mcp server with streamlit

- like there have 4 components 1. langGraph, 2. mcp client , 3. streamlit , 4. sqlite (four main components in this chat bot)

- problem ; mcp client tells that it will run only in async envirment, langgraph is comfortable with both sync and async but streamlit is foundment syncronus library and making it async is very hard (sir did) -> for that we have to make database async as well

* so in frontent there will only one place where you get to change is that we will use astream instead of stream function during workflow calling

## suggetion ;; if we are using mcp serve and client then we should not use stream for frontend
