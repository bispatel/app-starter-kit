import streamlit as st
from langchain.llms import OpenAI
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
import os
import shutil

# Specify the destination folder
destination_folder = 'files'

st.title('Bishwajit Search App')
uploaded_file = st.file_uploader("Upload a file")

if uploaded_file is not None:
    # Process the uploaded file
    # Save the uploaded file to the destination folder
    file_name = uploaded_file.name
    file_path = os.path.join(destination_folder, file_name)
    with open(file_path, "wb") as file:
        shutil.copyfileobj(uploaded_file, file)
    st.write("File uploaded successfully!")

openai_api_key=st.sidebar.text_input('OpenAI API Key')

def load_files(folder_path):
    files = os.listdir(folder_path)
    dataframes = []

    for file in files:
        if file.endswith('.csv'):
            dataframes.append(file)

    return dataframes
        
def generate_response(input_text):
  ##llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  ##st.info(llm(input_text))
  os.environ["OPENAI_API_KEY"] = openai_api_key
  #loader = CSVLoader(file_path='files/pokemon.csv')
  folder_path = 'files'
  ##loader = CSVLoader(folder_path=folder_path)
  st.info("Listing of files")
  dataframes = load_files(folder_path)
  st.info(dataframes)
  # Create data loaders for each CSV file
  data_loaders = [CSVLoader(file_path='files/'+filename) for filename in dataframes]
  st.info(data_loaders)
  #dataframes1 = []
  #st.info(loader)
  #dataframes1.append(loader)
  #llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  #st.info(llm(input_text))
  index_creator = VectorstoreIndexCreator()
  docsearch = index_creator.from_loaders(data_loaders)
  chain = RetrievalQA.from_chain_type(llm=OpenAI(),chain_type="stuff",retriever=docsearch.vectorstore.as_retriever(),input_key="question")
  response=chain({"question":input_text})
  st.info(response['result'])
 

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
    
    