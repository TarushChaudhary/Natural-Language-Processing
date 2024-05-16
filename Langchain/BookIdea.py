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

st.title('Book Title Generator')
prompt = st.text_input("Enter Your Prompt here")

#Prompt Template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='Write Me a book title about {topic}'
)

#Prompt Template to Generate Synopsis
syn_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'],
    template='Write Me a book synopsis based on this title TITLE: {title} while leveraging this wikipedia research:{wikipedia_research}'
)

#Memoryl
title_memory = ConversationBufferMemory(input_key= 'topic', memory_key='chat_history')
syn_memory = ConversationBufferMemory(input_key= 'title', memory_key='chat_history')


# LLMs
llm = OpenAI(temperature=0.8)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key= 'title', memory=title_memory)
syn_chain = LLMChain(llm=llm, prompt=syn_template, verbose=True, output_key= 'synopsis', memory=syn_memory)

wiki = WikipediaAPIWrapper()

#Show Response if theres a Prompt
if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    syn = syn_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title)
    st.write(syn)

    with st.expander('Title History'):
        st.info(title_memory.buffer)


    with st.expander('Synopsis History'):
        st.info(syn_memory.buffer)
    
    with st.expander('Wikipedia Research'):
        st.info(wiki_research)



