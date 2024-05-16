from apikey import apikey
import os
import openai
openai.api_key = apikey

chatlog = []



while True:
    chatlog.append({"role": "system", "content": "talk like a chatbot"})
    text = input()
    if text.lower() == "quit":
        break
    else:
        chatlog.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = chatlog
            
            )
        assistantresponse = response["choices"][0]['message']['content']
        print("ChatGPT: ", assistantresponse.strip("\n").strip()) 
        chatlog.append({"role": "assistant", "content": assistantresponse.strip("\n").strip()})
        


    
 
