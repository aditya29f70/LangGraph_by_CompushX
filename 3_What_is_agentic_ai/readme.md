## What is Agentic AI?

-> Agentic Ai is a type of Ai that can take up a task or goal from a user and then work toward completing it on its own, with minimal human guidance.

-> It plans, takes action, adapts to changes, and seeks help only when necessary

## Key Characteristics

- how you identify a ChatBot is AgenticAi system. => see pic-1

- it has 6 trades or characteristic

* if someone put a agent ai model and asked you to identify is this agentic or not ;; you have to see these six things are working on it or not

1. Autonomous
2. Goal Oriented
3. Planning
4. Reasoning
5. Adaptability
6. Context Awareness

## 1. Autonomy:

-> Autonomy refers to the AI system's ability to make decisions and take actions on its own to achieve a given goal, without needing step-by-step human instructions.

1. Our Ai recruiter is autonomous

2. It's pro-active

3. Autonomy in multiple facets
   a. Execution
   b. Decision making
   c. Tool usage

4. Autonomy can be controlled
   a. **Permission Scope** - Limit what tools or actions the agent can perform independently . (can screen candidates, but needs approval before rejecting anyone)

b. **Human-in-the-loop** (HITL) - Insert checkpoints where human approval is required before continuing. (can i post this JD)

c. **Override Constrols** - Allow users to stop, pause, or change the agent's behaviour **at any time.** (pause screening command to halt resume processing.)

d. **Guardrails/Policies** - Define hard rules or ethical boundaries the agent must follow. (Never schedule interviews or weekends)

5. Autonomy can be dangerous

a. The application autonomously sends out job offers with incorrect salaries or terms.

b. The applications shortlists candidates by age or nationality anti-discrimination laws.

c. The application spending extra on Linkedin ads.

## 2. Goal Oriented

-> Being goal-oriented means that the AI System operates with a persistent objective in mind and continuously directs its actions to achieve that objective , rather that just responding to isolated prompt.

1. Goals acts as compass of Autonomy
2. Goals can come with constrints (like you can say;; i want to hire a backend engineer with 2-4 year experience)
3. Goals are stored in core memory (see_pic 2)

4. Goals can be altered (you can change the anything about goals like if you want hiring not from linkeding instead hiring from freelancing you can change at anytime)

## 3. Planning;

- vvmp step which if you tell what agentic ai does ;; it basically first planning (how to achieve that goal)+ step2 start execution this two step is iterative
- in between this loop if you realise that any step is not possible to do it will start looping from start point (planning)

-> Planning is the agent's ability to break down a high-level goal into a structured sequence of actions or subgoals and decide the best path achieve the desired outcome.

- step 1: Generating multiple condidate plans (what is this? , this give you a fact that if a query to come to agentic ai will make multiple plain not one to achieve that goal **those plans are called conidate plans**)
- so planning is search proble where you have a inital state(your companey want a backend eng) and have final state (your companey get a backend eng);; so multiple state exsist bw them

- - Plan A (first condidate plan) : Post JD on Linkedin, GitHub Job, AngelList
- - Plan B (second condidate plan): Use internal referrals and hiring agencies

- step 2: Evaluate each plan (to choice best plan)
- - Efficiency (Which is faster?)
- - Tool Availability (which tools are available)
- - Cost (Does it require premium tools?)
- - Rish (Will it fail if we get no applicants?)
- - Alignment with constraints (remote-only? budget?)

steps3: Select the best plan with the help of :

- - **Human-in-the loop** input (e.g "Which of these options do you prefer?")
- - A pre-programmed **policy** (eg. "Favor low-cost channels first")

## 4. Reasoning

- so we know there is two imp step planning(find condidate plans and evalute them to get best of them) then sec one is execution so in both of them we use Reansong to understand goal to generate diff plan and after evaluation (also use reasoning) we also use reasoning to find which those tool should we use.

-> **Reasoning** is the cognitive process through which an agentic ai system interprets information,draw conclusions,and make decisions -- both while planning ahead and while executing actions in real time.

- Reasoning During Planning:

1. **Goal Decomposition** - Break down options (3 candidates match -> schedule 2 best, reject 1)
2. **HITL handling** - Knowing when to pause and ask for help (Unsure about salary range)
3. **Error handling** - Interpreting tool/API failures and recovering

## 5. Adaptability

-> Adaptablity is the agent's ability to modify its plans, strategies, or actions in response to unexpected conditions -- all while staying aligned with the goal.

1. Failures (calendar API)
2. External feedback (Less no of applications);; **every agentic ai works in a envirement eg if we have made a agent for chess so that chess board is our envirement**
   -> so some time something bad is happend around our env so ai agent has to adapt those prob and give feedback about it
3. Changing goals (Hiring a freelancer);; at the mid process you suddenly said that you don't want to hire backend engineer you want a freelance to it has to adapt that

## 6. Context Awareness (without context awareness , you can't ask any working process have been done or not if it is not remembering those previous things)

-> Context awareness is the agent's ability to understand, retain, and utilize relavant infomation from the ongoing task, past interactiions, user preferences, and environmetal cues to make better decision throughout a multi-step process.

1. Types of context (what kind of context awareness it takes or remembers)
   a. The original goal
   b. Progress till now + Interaction history (job description was finalized and posted to linkedin and github jobs)
   c. Environment state (Number of applications so far = 8 or linkedin promotion ends in 2 days)

d. Tool responses (Resume parser -> "Candidate B has 3 years Django + AWS experience or Calendar API -> "No conflict at 2 PM Wednesday);; go under short term memory

e. User specific preference (prefers remote-first condidates or Likes receiving interview questions in a google doc)

f. Policy or Guardrails (do not send offer without explicit user approval or never use platforms that requrie paid ads unless approved);; these things help to constrain human interaction for some related questions; those will be gotten through these policies;; ;; go uner long term memory

2. Context awareness is implemented through memory (these all above things are implimented or saved in memory)

- agentic ai has two kind of memory (like computer ram , hard disc)

3. Short term memory (store current session related information)
4. Long term memory

## core high level components of agentic ai;; (you can see these components in most of the agentic ai system)

1. Brain
2. orchestrator
3. Tools
4. Memory
5. Supervisor

## 1. Brain (LLM);; it works for

- **Goal Interpretation** -> understands user instructions and translates them into objectives.
- **Planning** -> Breaks down high-level goals into subgoals and ordered steps.
- **Reasoning** -> Makes decisions, resolves ambiguity, and evaluates trade-offs.
- **Tool Selection** -> Choose which tool(s) to use at a given step.
- **Communication** -> Generates natural language output for humans or other agents.

- there is also some components like , 1. planner, 2. evalutor

## 2. Orchestrator;;(it execute your plan;; planing is happened by llm);; it kinds of project manager of agent ai system

- --> which steps happend after which steps for the planing it decides; in the basis of step1 output you can go step2 or 3 those rules or written in Orchestrator (you design it using LangGraph framework)
- Task Sequencing -> Determines the order of actions (step-1 -> step-2 ->..)
- conditional Routing -> Directs flow based on context (eg. if failure, retry or escalate)
- Retry Logic -> Handles failed tool call or reasoning attempts with backoff.
- Looping and iteration -> Repeats steps (eg. Keep checking job apps untill 10 are received).
- Delegation -> Decides whether to hand off work to tools, LLM, or Human.

## 3. Tools

- **External Actions** -> Perform Api call (e.g. post a job, send an email, trigger onboarding).
- **Knowledge Base Access**(one kind of tool) -> Retrieve factual or domain-specific information using RAG or Search tools to ground responses.

## 4. Memory

- **Short-term Memory** Maintains the active session's context -- recent user messages, tool calls, and immediate decisions.
- **Long-term memory** Persists high-level goals, past interactions, user preferences, and decision across sessions.
- **State Tracking** Monitors progress: what's completed, what's pending (e.g. "JD posted", "offer sent").

## 5. Supervisor (it is who which help agent to work with humans)

- **Aproval Requests(HITL)** -> Agent check with human before high-risk actions (eg. sending offers).
- **Guardrails Enforcement** -> Blocks unsafe or non-compliant behavior.
- **Edge Case Escalation** -> Alerts humans when uncertainty/conflict arises. (like you said you want IIT/Nit student but someone whose resume is great but not belongs to IIT/nit so that is basically escalation case or confict case so your agent will info you regarding that )
