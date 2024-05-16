import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper



os.environ['OPENAI_API_KEY'] = apikey

#App  Framework

st.title('Broken Text Corrector')
prompt = st.text_input("Enter Your Prompt here")

#Prompt Template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='Correct and rewrite the given sentence: {topic} '
)

#Memoryl
title_memory = ConversationBufferMemory(input_key= 'topic', memory_key='chat_history')


# LLMs
llm = OpenAI(temperature=0.8)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key= 'title', memory=title_memory)


#Show Response if theres a Prompt
if prompt:
    title = title_chain.run(prompt)

    st.write(title)
    
    with st.expander('Title History'):
        st.info(title_memory.buffer)

