import streamlit as st
from langchain.llms import OpenAI
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
import os
import pandas as pd

st.title('Bishwajit Search App')

openai_api_key=st.sidebar.text_input('OpenAI API Key')

def load_files(folder_path):
    files = os.listdir(folder_path)
    dataframes = []

    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)
            dataframes.append(df)

    return dataframes
        
def generate_response(input_text):
  ##llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  ##st.info(llm(input_text))
  os.environ["OPENAI_API_KEY"] = openai_api_key
  ##loader = CSVLoader(file_path='pokemon.csv')
  folder_path = 'files'
  ##loader = CSVLoader(folder_path=folder_path)
  dataframes = load_files(folder_path)
  index_creator = VectorstoreIndexCreator()
  docsearch = index_creator.from_loaders(dataframes)
  chain = RetrievalQA.from_chain_type(llm=OpenAI(),chain_type="stuff",retriever=docsearch.vectorstore.as_retriever(),input_key="question")
  response=chain({"question":input_text})
  st.info(response['result'])
  print(response['result'])

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)