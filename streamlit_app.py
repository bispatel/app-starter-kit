import streamlit as st
from langchain.llms import OpenAI
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
import os

st.title('Bishwajit Search App')

##openai_api_key = st.sidebar.text_input('OpenAI API Key')
os.environ['OPENAI_API_KEY']='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'

def generate_response(input_text):
  #llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  #st.info(llm(input_text))
  loader = CSVLoader(file_path='pokemon.csv')
  index_creator = VectorstoreIndexCreator()
  docsearch = index_creator.from_loaders([loader])
  chain = RetrievalQA.from_chain_type(llm=OpenAI(),chain_type="stuff",retriever=docsearch.vectorstore.as_retriever(),input_key="question")
  response=chain({"question":input_text})
  st.info(response['result'])
  print(response['result'])

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
 # if not openai_api_key.startswith('sk-'):
 #   st.warning('Please enter your OpenAI API key!', icon='⚠')
 # if submitted and openai_api_key.startswith('sk-'):
  generate_response(text)