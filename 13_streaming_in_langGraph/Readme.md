## We will see a problem and how can we solve it

- like streaming problem , when we search like write a 500 words easy it takes tike go generate on backend and once it is generated then send completly at a time on frontend - but we want **streaming** -> we want to see how llm is generating things token by token

## Now let discuess about **streaming**

- In LLM, streaming means the model start sending tokens (words) as soon as they're generated, instead of waiting for the entire response to be ready before returning it.

## Why streaming

1. Fast response time - low drop-off rates
2. mimics human like conversation (build trust, feels alive and keeps the the user enagaged)
3. Important for multimodel UIs
4. better ux for long output such as code
5. you can cancel midway saving tokens
6. you can interleave UI updates , e.g. show "Thinking..." show tool result

12:00
