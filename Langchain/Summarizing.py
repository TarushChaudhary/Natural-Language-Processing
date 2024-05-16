import openai
import os

openai.api_key = apikey

def getcompletions(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0.2
    )

    return response.choices[0].message["content"]

text = f""""

hello this is some random placeholder text.

"""

prompt = f"""

You are tasked with summarizing the given text in 5 words or less. The text provided is delimited by triple backticks
```{text}```

"""
print(getcompletions(prompt))