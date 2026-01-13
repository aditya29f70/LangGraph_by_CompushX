## learn how to build **Parallel workflow**
* try to solve two workflow
* first -> simple parallel workflow (non-llm based)
* second -> llm workflow (bit difficult) ;; used some concepts from langChain

## 1. simple Parallel workflow 
* related to cricket
* so we have to build a such application where we will be gotten some input related to a bats-man -> like in a particular ining , how much run they got, how much boll they have played, how much 4 they get and how much 6 they get

* and in output you have to calculate multiple things
* 1. have to calculate what it's Sr (Strike Rate) (It shows how fast a batsman scores runs.) -> Strike Rate (SR)=(Runs Scored /Balls Faced​)×100
* 2. Runs in boundary % (like they have gotten 100 run in it they got 50 run by 4s and 6s then then runs_in_boundary= 50/100*100= 50%)

* 3. lly you can also find balls-per-boundary(after how much ball bats-men hit the ball boundary, like they playied 10 bolls and hit 4 time 4s or 6s -> 10/4 =2.5 -> means every 2 or 3 ball bats-men hit a 4 or 6) parallely 

* and you can think that these three can be calculate parallely by using input data

* at the last we make a summary node , which will summaries these three things

* now lets talk about state of this workflow
* that input values (runs, balls, 4s, 6s)
* and Sr(syc-rate), boundary %, balls per boundar
* and at the last we will have summary


## Import things when we work with parallel workflow
*  after invoking you workflow you often get an error like -> InvalidUpdateError
* what we have mistaked it that our eact calculative node returing **state** after calculation
* each things in state are returned three time;; what problem with parallel workflow is that after parallel node execuation you have done any thing with an attribute of typedDict
* and when langgraph recived a state from diff node at time it assume that something have been changed in every attribute however there are not any chnaged in any step but it assume it first so after that it confused
* so this thing is conflict that which state value should  take

* solution is that you should not send whole output(state) from each calculation node 
* instead you should only send those attribute which have been changed (calculated)

* basically we will send partial state not whole

* so rather than sending state we will send a dict with that attributes those have been changed