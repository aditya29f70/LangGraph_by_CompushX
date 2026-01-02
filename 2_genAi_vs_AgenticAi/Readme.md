## What is GenAi:
-> Refers to a class of artificial intelligence models that can create new content - such as text, image, audio, code, or video -- that resembles human(means it feels like human generated content) - **created data**.

* EG; LLMs based app like Chat GPT
* Diffusion models for images
* Code generation LLMs like codeLLama

* TTS (text-to-speech(human like) models) models like ElevenLabs

* Video gen models like Sora (text-video(short video))

## Generative Ai vs Traditional Ai(old ai model or classical, deep learning models)

* Traditional Ai is about **finding patterns** in data and giving predictions.(eg work on classificaion models)

* Generative Ai is about **learning the distribution**(try to understand data ki fhitrat or nature) of data so that it can generate a new sample from it. 
* Eg. like you gave multiple cat pic to it then it will try to analys how cat looks it's distribution, and after that it can easly generate a similar kind of sample
* good thing about GenAi -> GenAi is that it can mimic humans;; it's outcome feels like human generated

## what are the areas where genAi is contineously being used. (Application Areas)

* Creative and Business writing.
* software development
* Customer support 
* Education;; doubt clears;; assignment ..
* Designing ;; advatisment

* GenAi is constantly evolving and improving.

## now we take a problem and try to solve using genAi
* Goal(you are Hr and need to recrute) - to hire a backend engineer;; what are the steps have to follow:
* * Creating a JD
* * Posting the JD to a job platform
* * Shortlisting for interview based on there resume, try to have top 50 condidate
* * interviewing
* * Rolling an offer letter
* * OnBoarding

* now try to implement these using GenAi and understand how GenAi can help for this prob

* let our companies have given a chatbot (companies's chatBot)
## LLM based ChatBot - JD drafting
* now we have JD
* now ask to that LLM , where we can post this jd or plateforms where we can post this
* manually go to linkdin and naukari to post this jd
## LLM Based Chatbot - job posting
## LLM Based ChatBot - shortlisting
* llm will give ideal on the basis of those ideal we can select backend dev (like it has to knowledge about cloud , backend frame work etc)

* so on the basis of those ideals we have selected some condidates

## LLM Based ChatBot -- Scheduling
* now tell LLM can you draft a email, to invite those condiate for interview.

* now we have a sample email

## LLM based ChatBot -- interviewing
* you can ask for questions (what kind of questions should they ask to condidate) --> question banks

* now you can finally selected some condidate and you have to now send offer later

## LLM Based ChatBot -- Drafting Offer;; can you help me draft offer latter

## is this complete -no ;; there certain problems
* Chat bot and human interaction ;; these whole process is **Reactive** --> when we give prompt to chatbot then only it retuning response;; it's no pro-active

* or it is not understanding the flow (what it should do next)

* No memory (our chat-Bot don't have any memory) so don't have context aware

* this chatBot is giving us very Generic Advice (it would be good it tht jd will be generated more specific on our busineess)

* Can't take actions (don't have tool calling access)

## now try to improve this problem specifically on 'generic advice' at least it should give advice more specific to our business

## Chatbot2 (now it is connected to our componey **knowledge_base**)

* what would be knowledge_base
* (JD Templates)
* * 1. Past JD's used by the componey
* * 2. Example of high performing JD's
* * 3. Variations for remote vs in-office, junior vs senior

* (Hiring Strategies)
* * 1. Best platform for hiring
* * 2. Best practices for hiring
* * 3. Internal salary band
* * 4. internal checklist to hire for various profiles
* * 5. Interview question banks for various profiles

* (On boardig Checklist) 
1. Offer letter template
2. Welcome email template
3. Employee policies

## now this chatBot is called Rag based ChatBot

## now every user question we have our business data (context) so chat bot response would be more specific or relavent to our business

## still have problems
1. Reactive
2. memory (don't have context awareness, like it don't remember what we discussed tomorrow)

3. Specific Advice (done)
4. can't take action itself 

## chatbot3;; (can take action itself;;like posting job on diff platforms) --> integrated with diff tools like email , calender, linkdin api etc

* now this kind of chatBot is called -> Tool Augmented ChatBot 

* still user have to tell what is flow and what probleming is coming and solving statement then after tools work on those problem.

## problem 
* it is still reactive (we are telling what it has to do, not it is asking what it sould do next)
* memory (context awareness)

* can't adapt ;; like it is not analysing what is problem is coming in the flow, and following alternative path if some problem is comming


## ChatBot4 (all probs are solved) and called -> Agentic Ai chatBot
-> have become -> pro-active
* after only telling that 'i want to hire a backend engineer' -> it will plan every things and divide those into steps and gona implements those 


## conclusion
1. Generative Ai is about creating content, agentic Ai is about solving a goal

2. GenAi is reactive, Agentic ai is pro-active (automous) /human come but only for aproval

3. GenAi is a building block of Agentic Ai

# GenAi is capability and AgenticAi is behaviour





















