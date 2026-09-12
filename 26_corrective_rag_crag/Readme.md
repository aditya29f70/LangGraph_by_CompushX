## Why crag if rag works great

-> in rag llm start **blindly trast** on retrieved docs, if retrieved docs are not relavent to query then we can get unrelated answer

let eg vector Db is about ML docs and your query is about llm then your llm is froced to answer from unrelated retrieved docs ;; this problem is solved by crag

- if llm doesn't get related docs then it tries to answer from its paramatric knowledge and if it doen't have any konwledge then we get unrelavent ans (halusination)

* so have crag resolve it -> it doesn't let retieval to give retrieved docs to llm instead it adds one more layer/model after retrieval calls **retrieval evaluator** -> it works is to check whether retrieved docs are relavent to query or not ,those are related will be given to llm

* this retrieval evaluator faces three kind of docs -> 1. relavent (then works will be like noraml rag), 2. not relavent (llm goes to external knowledge search if added+ llm parameteric knowledge), 3. ambiguous (so relavent docs only are sent to llm + use external sources)

* so crag is not blindly trasting retrieved docs;;

* so we will build crag from scrach
