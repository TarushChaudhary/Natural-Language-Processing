#imports
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import os
from apikey import apikey

#building the environment
os.environ["OPENAI_API_KEY"] = apikey

#reading the pdf
pdfdoc = open(r'C:\Users\tarus\Desktop\STUDY MATERIAL\Self\Bible.pdf', mode='rb')
reader = PdfReader(pdfdoc)

#extracting raw text 
raw_text  = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

#splitting text into chunks to avoid openai token limit

text_splitter = CharacterTextSplitter(
    separator= "\n",
    chunk_size = 1000,
    chunk_overlap = 200, 
    length_function = len
)    
texts = text_splitter.split_text(raw_text)

#adding embeddings
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(texts, embeddings)

#creating chain 
chain = load_qa_chain(OpenAI(), chain_type="stuff")


#generating Query 
query = "who is the author of this book"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)
print(docs)
