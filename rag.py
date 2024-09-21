import cohere
import langchain
import pinecone 
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains.question_answering import load_qa_chain
import os
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
import streamlit as st
from langchain.chains import RetrievalQA  


from dotenv import load_dotenv
load_dotenv()

## load the GROQ API Key
#os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['PINECONE_API_KEY=']=os.getenv("bd737763-f992-40b3-923f-874a79415b24")

os.environ['cohere_api_key']=os.getenv("3ABbfdoL7YGQmDTbxUMoLY5AZIYV0mntXkr25LW7")

# Initialize the LLM with Llama 3.1 model
llm = ChatOllama(
    model="llama3.1",
    temperature=0,
)

prompt = PromptTemplate(
    template="""You are an assistant for question-answering tasks.
    Use the following documents to answer the question.
    If you don't know the answer, just say that you don't know.
    Use three sentences maximum and keep the answer concise:
    
    Answer the questions based on the provided context only.
    Please provide the most accurate respone based on the question
    <context>
    {context}
    <context>
    Question:{input}

    """

)

def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.loader=PyPDFDirectoryLoader() ## Data Ingestion step
        st.session_state.docs=st.session_state.loader.load() ## Document Loading
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors=pinecone.from_documents(st.session_state.final_documents,st.session_state.embeddings)
st.title("RAG document Q&A")
user_prompt=st.text_input("Enter your query:")


# File upload
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Vector Database is ready")


if user_prompt:
    document_chain=qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    #retriever=docsearch.as_retriever()
)
    retriever=st.session_state.vectors.as_retriever()
    #retrieval_chain=create_retrieval_chain(retriever,document_chain)
    
    
