## we are going to add one more feature in our chat bot -> **resume chat**

- like this feature we get to see in chatgpt or any ai application that we can creat new converstion or resume any previour chat

* we don't need to change anythings on backend side

## loadmap to add that resume feature

-> add a sidebar with title + A Start chat button + A title named 'My conversations'

-> Generate dynamic thread id and add it to the session

-> display the tread id in sidebar

---

-> add a new chat button
-> on click of new chat open a new chat window

- generate a new thread_id
- save it in session
- reset message history

---

-> create a list of store all thread_ids
-> load all the thread ids in the sidebar
-> convert the side bar text to clickable buttons

---

-> on click of a particular thread id load that particular conversation
