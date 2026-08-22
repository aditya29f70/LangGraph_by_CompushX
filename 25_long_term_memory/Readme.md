how to add LTM in our chat-bot

- we don't get idea of user in a single converstion , having diff conversation help us to know about user
- a single thread cann't capture all things about a user

- so for implementing LTM we use a storage (can be database) and on every conversation with chat we don't only ask the question instead we also ask is this prompt also capture some info about user which can help in the future and we store those in that memory

* and good thing is that, this memory is persistant (to be stored for a long time) --> and this storage is called LTM

* and our agent always try to go through this memory on every query to make its answer more personalise
  eg if agent has noticed that i follow python as programming lang and some day if i ask agent to any programming question then it will once check this memory and make the ans more personlise

* In langgraph LTM concept is implemented using Store and its code we get to see in this calls -> BaseClass -> and it is an abstract class and this abstract class is named as -> 'BaseStore'

* and at this base store there are some functionality mentioned like what are things it can do eg
* - It can create new memory
* - search in existing memory
* - edit existing memory
* - delete existing memory

* and multiple class inherit this base class eg
* - InMemoryStore (It store memory in ram) # this is only for test perpose
* - PostgreStore # use in production
* - redisStore # production grade implementation

## Let implement it (coding)

- first try to make 'memoryStore' -> try to create store and search
- then try to integrate with langgraph

- and using it we will add this concept at our chat-bot will use create memory and read

## what is namespace ? it is like folder inside drive , we use to arrange our files lly we use 'namespace' to organise memory

eg, (user1, u1) ; means at user1 folder(memory) we have build a user 1(file)

- lly (user1, u2) ;; saving user2 to at same memory namespace

* now (user, u1, profile) -> so here we are adding one more namespace inside user1 namespace
* or (user, u1, preperance) namespace ;;
* and inside these namespace we can store uesr related memory like its profile info, preferance info

## so namespace is used to organise diff memory inside a memory space;; and **namespace is alway created using tuple**

eg. namespace= ("user", "u2")

- question-> how to store momory inside this namespace -> using **put** method ; basically it insert/create a new memory inside a namespace; its inputs are -> 'namespace'(where we need to create memory), 'Key' (that memory unique key), 'value' (that memory value)
