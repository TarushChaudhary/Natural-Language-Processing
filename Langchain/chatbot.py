from apikey import apikey
import os
import openai

openai.api_key = apikey

def getCompletions(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "system", "content": "You must talk as if you snoop dogg"},
        {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
 l= model,
        messages=messages,
        temperature = 0.2
    )
    return response.choices[0].message["content"]

text = input("Enter Text To be Summarized: ")
prompt = f"""
Summarize the text delimited by triple backticks \ 
into One Paragraph.
```{text}```
"""
response = getCompletions(prompt)
print(response)