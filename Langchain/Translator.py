import openai
import os

openai.api_key = apikey

def getcompletions(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt},
                {"role": "system", "content": " You are a Translator whos task is to translate the given text into the language mentioned"}]
    response = openai.ChatCompletion.create( 
        model = model,
        messages = messages,
        temperature = 0.2
    )

    return response.choices[0].message["content"]

# prompt = f"""
# Translate the following English text into french: \
# ```Hi My Name is Arty```
# """

# response = getcompletions(prompt)
# print(response)

# prompt = f"""
# Identify what language this is and translate it: \
# ```kaun hai tu bhai```
# """
# response = getcompletions(prompt)
# print(response)

user_messages = [
    "I want Some Tea",
    "je m'appelle tarush",
    "kya ho rha hai",
    "My foot hurts"
]

for i in user_messages:
     prompt = f"tell me what language this is: ```{i}```"
     language = getcompletions(prompt)
     print(f"Original Message ({language}): {i}")
     prompt = f"""
     Translate the following text into english and hindi(in english script): \
     ```{i} ```
     """

response = getcompletions(prompt)
print(response, "\n")


# CANNOT RUN LOOPS ON FREE TRIAL OF GPT-3.5-TURBO NEED TO INCREASE RATE LIMIT, CURRENT LIMIT 3 PROMPTS/20s